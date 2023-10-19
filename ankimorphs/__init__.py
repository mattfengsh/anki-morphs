from functools import partial

from aqt import gui_hooks, mw
from aqt.browser.browser import Browser
from aqt.qt import (  # pylint:disable=no-name-in-module
    QAction,
    QDesktopServices,
    QKeySequence,
    QMenu,
    QUrl,
)
from aqt.reviewer import Reviewer
from aqt.toolbar import Toolbar
from aqt.utils import tooltip

from ankimorphs import (
    browser_utils,
    recalc,
    reviewing_utils,
    settings_dialog,
    toolbar_stats,
)
from ankimorphs.ankimorphs_db import AnkiMorphsDB
from ankimorphs.config import AnkiMorphsConfig, get_config
from ankimorphs.toolbar_stats import MorphToolbarStats

# A bug in the anki module leads to cyclic imports if these are placed higher
import anki.stats  # isort:skip pylint:disable=wrong-import-order
from anki import hooks  # isort:skip pylint:disable=wrong-import-order
from anki.collection import Collection  # isort:skip pylint:disable=wrong-import-order
from anki.cards import Card  # isort:skip pylint:disable=wrong-import-order


# Semantic Versioning https://semver.org/
# TODO store somewhere other than mw, makes testing problematic
mw.ANKIMORPHS_VERSION = "0.1.0-alpha"  # type: ignore

TOOL_MENU = "am_tool_menu"
BROWSE_MENU = "am_browse_menu"
CONTEXT_MENU = "am_context_menu"


def main() -> None:
    # Support anki version 2.1.50 and above
    # Hooks should be placed in the order they are executed!

    # Adds the 'U: A:' to the toolbar
    gui_hooks.top_toolbar_did_init_links.append(add_morph_stats_to_toolbar)

    # Update the toolbar stats
    gui_hooks.profile_did_open.append(redraw_toolbar_wrapper)

    gui_hooks.profile_did_open.append(init_tool_menu_and_actions)
    gui_hooks.profile_did_open.append(replace_reviewer_functions)
    gui_hooks.profile_did_open.append(init_browser_menus_and_actions)

    # This stores the focus morphs seen today, necessary for the respective skipping option to work
    gui_hooks.reviewer_did_answer_card.append(mark_morph_seen_wrapper)

    gui_hooks.profile_will_close.append(reset_seen_morphs)


def reset_seen_morphs() -> None:
    AnkiMorphsDB.drop_seen_morph_table()


def redraw_toolbar_wrapper() -> None:
    # wrapping this makes testing easier because we don't have to mock mw
    assert mw
    mw.toolbar.draw()


def init_tool_menu_and_actions() -> None:
    assert mw

    for action in mw.form.menuTools.actions():
        if action.objectName() == TOOL_MENU:
            return  # prevents duplicate menus on profile-switch

    am_config = AnkiMorphsConfig()

    settings_action = create_settings_action(am_config)
    recalc_action = create_recalc_action(am_config)
    guide_action = create_guide_action()
    changelog_action = create_changelog_action()

    am_tool_menu = create_am_tool_menu()
    am_tool_menu.addAction(settings_action)
    am_tool_menu.addAction(recalc_action)
    am_tool_menu.addAction(guide_action)
    am_tool_menu.addAction(changelog_action)

    # test_action = create_test_action()
    # am_tool_menu.addAction(test_action)


def init_browser_menus_and_actions() -> None:
    am_config = AnkiMorphsConfig()

    view_action = create_view_morphs_action(am_config)
    learn_now_action = create_learn_now_action(am_config)
    browse_morph_action = create_browse_same_morph_action()
    browse_morph_unknowns_action = create_browse_same_morph_unknowns_action(am_config)
    already_known_tagger_action = create_already_known_tagger_action(am_config)

    def setup_browser_menu(_browser: Browser) -> None:
        browser_utils.browser = _browser

        for action in browser_utils.browser.form.menubar.actions():
            if action.objectName() == BROWSE_MENU:
                return  # prevents duplicate menus on profile-switch

        am_browse_menu = QMenu("AnkiMorphs", mw)
        am_browse_menu_creation_action = browser_utils.browser.form.menubar.addMenu(
            am_browse_menu
        )
        assert am_browse_menu_creation_action
        am_browse_menu_creation_action.setObjectName(BROWSE_MENU)
        am_browse_menu.addAction(view_action)
        am_browse_menu.addAction(learn_now_action)
        am_browse_menu.addAction(browse_morph_action)
        am_browse_menu.addAction(browse_morph_unknowns_action)
        am_browse_menu.addAction(already_known_tagger_action)

    def setup_context_menu(_browser: Browser, context_menu: QMenu) -> None:
        for action in context_menu.actions():
            if action.objectName() == CONTEXT_MENU:
                return  # prevents duplicate menus on profile-switch

        context_menu_creation_action = context_menu.insertSeparator(learn_now_action)
        assert context_menu_creation_action
        context_menu.addAction(view_action)
        context_menu.addAction(learn_now_action)
        context_menu.addAction(browse_morph_action)
        context_menu.addAction(browse_morph_unknowns_action)
        context_menu.addAction(already_known_tagger_action)
        context_menu_creation_action.setObjectName(CONTEXT_MENU)

    gui_hooks.browser_menus_did_init.append(setup_browser_menu)
    gui_hooks.browser_will_show_context_menu.append(setup_context_menu)


def mark_morph_seen_wrapper(reviewer: Reviewer, card: Card, ease: int) -> None:
    reviewing_utils.mark_morph_seen(card.id)


def replace_reviewer_functions() -> None:
    am_db = AnkiMorphsDB()
    am_db.create_seen_morph_table()
    am_db.con.close()

    # This skips the cards the user specified in preferences GUI
    Reviewer.nextCard = hooks.wrap(  # type: ignore[method-assign]
        Reviewer.nextCard, reviewing_utils.am_next_card, "around"
    )

    # Automatically highlights morphs on cards if the respective note stylings are present
    # hooks.field_filter.append(reviewing_utils.am_highlight)

    Reviewer._shortcutKeys = hooks.wrap(  # type: ignore[method-assign]
        Reviewer._shortcutKeys, reviewing_utils.am_reviewer_shortcut_keys, "around"
    )


def add_morph_stats_to_toolbar(links: list[str], toolbar: Toolbar) -> None:
    morph_toolbar_stats = MorphToolbarStats()

    links.append(
        toolbar.create_link(
            cmd="recalc_toolbar",
            label="Recalc",
            func=recalc.recalc,
            tip="AnkiMorph Recalc",
            id="recalc_toolbar",
        )
    )
    links.append(
        toolbar.create_link(
            cmd="unique_morphs",
            label=morph_toolbar_stats.unique_morphs,
            func=lambda: tooltip("U = Known Unique Morphs<br>A = All Known Morphs"),
            tip="U = Known Unique Morphs",
            id="unique_morphs",
        )
    )
    links.append(
        toolbar.create_link(
            cmd="all_morphs",
            label=morph_toolbar_stats.all_morphs,
            func=lambda: tooltip("U = Known Unique Morphs<br>A = All Known Morphs"),
            tip="A = All Known Morphs",
            id="all_morphs",
        )
    )


def create_am_tool_menu() -> QMenu:
    assert mw
    am_tool_menu = QMenu("AnkiMorphs", mw)
    am_tool_menu_creation_action = mw.form.menuTools.addMenu(am_tool_menu)
    assert am_tool_menu_creation_action
    am_tool_menu_creation_action.setObjectName(TOOL_MENU)
    return am_tool_menu


def create_recalc_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&Recalc", mw)
    action.setShortcut(am_config.shortcut_recalc)
    action.triggered.connect(recalc.recalc)
    return action


def create_settings_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&Settings", mw)
    action.setShortcut(am_config.shortcut_settings)
    action.triggered.connect(settings_dialog.main)
    return action


def create_guide_action() -> QAction:
    desktop_service = QDesktopServices()
    action = QAction("&Guide (web)", mw)
    action.triggered.connect(
        lambda: desktop_service.openUrl(
            QUrl("https://mortii.github.io/anki-morphs/user_guide/intro.html")
        )
    )
    return action


def create_changelog_action() -> QAction:
    desktop_service = QDesktopServices()
    action = QAction("&Changelog (web)", mw)
    action.triggered.connect(
        lambda: desktop_service.openUrl(
            QUrl("https://mortii.github.io/anki-morphs/user_guide/changelog.html")
        )
    )
    return action


def create_learn_now_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&Learn Card Now", mw)
    action.setShortcut(am_config.shortcut_learn_now)
    action.triggered.connect(browser_utils.run_learn_card_now)
    return action


def create_browse_same_morph_action() -> QAction:
    action = QAction("&Browse Same Morphs", mw)
    action.triggered.connect(browser_utils.run_browse_morph)
    return action


def create_browse_same_morph_unknowns_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&Browse Same Unknown Morphs", mw)
    action.setShortcut(am_config.shortcut_browse_ready_same_unknown)
    action.triggered.connect(
        partial(browser_utils.run_browse_morph, search_unknowns=True)
    )
    return action


def create_view_morphs_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&View Morphemes", mw)
    action.setShortcut(am_config.shortcut_view_morphemes)
    action.triggered.connect(browser_utils.run_view_morphs)
    return action


def create_already_known_tagger_action(am_config: AnkiMorphsConfig) -> QAction:
    action = QAction("&Tag As Known", mw)
    action.setShortcut(am_config.shortcut_set_known_and_skip)
    action.triggered.connect(browser_utils.run_already_known_tagger)
    return action


# def create_test_action() -> QAction:
#     keys = QKeySequence("Ctrl+T")
#     action = QAction("&Test", mw)
#     action.setShortcut(keys)
#     action.triggered.connect(test_function)
#     return action
#
#
# def test_function() -> None:
#     assert mw
#     assert mw.col.db
#
#     am_db = AnkiMorphsDB()
#
#     # with am_db.con:
#     #     result = mw.col.db.execute("PRAGMA table_info('deck_config');")
#     #     print(f"morphs: {result}")
#
#     # with am_db.con:
#     #     result = am_db.con.execute("SELECT count(*) FROM Card")
#     #     print(f"Card_Morph_Map count: {result.fetchall()}")
#     #
#
#     # card_row = mw.col.db.execute(
#     #     """
#     #     SELECT *
#     #     FROM cards
#     #     WHERE id=1608533847636
#     #     """
#     # )
#     #
#     # print(f"result: {card_row}")
#
#     # am_db.print_table_info("Note_Type_Morph_Map")
#     am_db.print_table("Seen_Morphs")
#
#     # for row in am_db.con.execute(
#     #     "SELECT * FROM Morph ORDER BY highest_learning_interval DESC limit 100"
#     # ):
#     #     print(f"row: {row}")
#
#     am_db.con.close()


main()
