from __future__ import annotations

from pathlib import Path
from test import test_utils
from test.fake_configs import (
    config_inflection_evaluation,
    config_lemma_evaluation_lemma_extra_fields,
)
from test.fake_environment_module import (  # pylint:disable=unused-import
    FakeEnvironment,
    FakeEnvironmentParams,
    fake_environment_fixture,
)
from test.test_globals import (
    PATH_TESTS_DATA_CORRECT_OUTPUTS,
    PATH_TESTS_DATA_TESTS_OUTPUTS,
)
from typing import Any

import pytest

from ankimorphs.known_morphs_exporter import KnownMorphsExporterDialog

################################################################
#                CASES: EXPORTING KNOWN MORPHS
################################################################
# We can export known morphs based on their lemma, or
# lemma + inflection, so we test both.
# The KnownMorphsExporterDialog automatically checks which of
# those options should be used depending on whether the
# 'evaluate_morph_lemma' option is enabled in AnkiMorphsConfig.
################################################################
case_exporting_lemmas_params = FakeEnvironmentParams(
    actual_col="some_studied_lemmas_collection",
    expected_col="some_studied_lemmas_collection",
    config=config_lemma_evaluation_lemma_extra_fields,
    am_db="some_studied_lemmas.db",
)

case_exporting_inflections_params = FakeEnvironmentParams(
    actual_col="some_studied_lemmas_collection",
    expected_col="some_studied_lemmas_collection",
    config=config_inflection_evaluation,
    am_db="some_studied_lemmas.db",
)


@pytest.mark.parametrize(
    "fake_environment_fixture, only_store_lemma",
    [
        (case_exporting_lemmas_params, True),
        (case_exporting_inflections_params, False),
    ],
    indirect=["fake_environment_fixture"],
)
def test_known_morphs_exporter(  # pylint:disable=unused-argument
    fake_environment_fixture: FakeEnvironment,
    only_store_lemma: bool,
    qtbot: Any,
) -> None:
    exporter_dialog = KnownMorphsExporterDialog()

    if only_store_lemma:
        _file_name = "exported_known_morphs_lemmas.csv"
    else:
        _file_name = "exported_known_morphs_inflections.csv"

    correct_output_file = Path(
        PATH_TESTS_DATA_CORRECT_OUTPUTS,
        _file_name,
    )

    # sets the output dir
    exporter_dialog.ui.outputLineEdit.setText(str(PATH_TESTS_DATA_TESTS_OUTPUTS))

    # both 'correct_output' files have the occurrence column
    exporter_dialog.ui.addOccurrencesColumnCheckBox.setChecked(True)

    exporter_dialog._background_export_known_morphs()

    # the exported file has a dynamic name (includes datetime of creation), so we
    # have to retrieve it dynamically. The output dir should only contain one
    # file so this is pretty easy
    test_output_file = list(PATH_TESTS_DATA_TESTS_OUTPUTS.iterdir())[0]

    test_utils.assert_csv_files_are_identical(
        correct_output_file=correct_output_file, test_output_file=test_output_file
    )
