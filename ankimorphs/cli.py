import argparse
import codecs
import glob
import os.path
import signal
import sys
from collections import Counter
from typing import Optional, Union

from ankimorphs.morph_db import MorphDb
from ankimorphs.morphemizer import (
    CjkCharMorphemizer,
    JiebaMorphemizer,
    MecabMorphemizer,
    SpaceMorphemizer,
)


def die(msg):
    print(msg, file=sys.stderr)
    sys.exit(1)


def warn(msg):
    print(msg, file=sys.stderr)


CLI_PROFILE_PATH: Optional[Union[bytes, str]] = None


def profile_base_path() -> Optional[str]:
    """Dies if we can't find it."""
    if CLI_PROFILE_PATH is not None:
        return os.path.dirname(CLI_PROFILE_PATH)

    # To do this right we need, at a minimum, the logic in
    # the method aqt.profiles.ProfileManager._defaultBase .
    #
    # For now it's convenient to avoid depending on Anki's code, so
    # just pick a couple of branches of that logic that suffice for
    # me and many users, with a clear error message.
    candidates = [
        os.path.expanduser("~/Anki"),
        os.path.expanduser("~/Documents/Anki"),
    ]
    for path in candidates:
        if os.path.exists(path):
            return path

    die(
        """\
This script is too naive to find your Anki folder.  Tried:
  %s
Try passing the profile folder explicitly with `--profile`.
"""
        % ("\n  ".join(candidates))
    )
    return None


def profile_path():
    """Look for the Anki profile.  Dies unless it finds exactly one."""
    if CLI_PROFILE_PATH is not None:
        path = CLI_PROFILE_PATH
        if not os.path.isdir(path):
            die("No such folder at Anki profile path (from --profile): " + path)
        dbs_path = os.path.join(path, "dbs")
        if not os.path.isdir(dbs_path):
            die("No MorphMan dbs folder in Anki profile (from --profile): " + dbs_path)
        return path

    base = profile_base_path()

    pattern = os.path.join(base, "*", "dbs", "")
    db_paths = glob.glob(pattern)
    if not db_paths:
        die(f"No candidate MorphMan db paths in Anki folder: {(pattern,)}")
    if len(db_paths) > 1:
        die(f"Multiple possible MorphMan db paths: {(' '.join(db_paths),)}")

    return os.path.dirname(os.path.dirname(db_paths[0]))


def db_path(db_name):
    return os.path.join(profile_path(), "dbs", db_name + ".db")


MIZERS = {
    "space": SpaceMorphemizer(),
    "mecab": MecabMorphemizer(),
    "cjkchar": CjkCharMorphemizer(),
    "jieba": JiebaMorphemizer(),
}


def cmd_dump(args):
    db_name = args.name
    inc_freq = bool(args.freq)

    path = db_path(db_name)
    if not os.access(path, os.R_OK):
        die(f"can't read db file: {path}")
    db = MorphDb(path)  # pylint:disable=invalid-name

    for morph in list(db.db.keys()):
        m_formatted = morph.show().encode("utf-8")
        if inc_freq:
            print(f"{db.frequency(morph)}\t{m_formatted}")
        else:
            print(m_formatted)


def cmd_count(args):
    files = args.files
    mizer = MIZERS[args.mizer]

    freqs = Counter()
    for path in files:
        with codecs.open(path, encoding="utf-8") as file:
            for line in file.readlines():
                freqs.update(mizer.get_morphemes_from_expr(line.strip()))

    for morph, count in freqs.most_common():
        print(f"{count}\t{morph.show().encode('utf-8')}")


def fix_sigpipe():
    """Set this process to exit quietly on SIGPIPE, like a good shell-pipeline citizen."""
    # For context, see e.g. https://stevereads.com/2015/09/25/python-sigpipe/.
    signal.signal(
        signal.SIGPIPE,  # pylint: disable=E1101 # Windows doesn't have these signals
        signal.SIG_DFL,
    )


def main():
    """Usage: `mm --help`.

    This function is meant to be invoked via the tiny wrapper script `mm`.
    """
    fix_sigpipe()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--profile",
        metavar="DIR",
        help="path to Anki profile (if absent, we try some guesses)",
    )
    subparsers = parser.add_subparsers(title="subcommands")

    p_dump = subparsers.add_parser(
        "dump",
        help="dump a MorphMan db in text form",
        description="Dump a MorphMan database to stdout in a plain-text format.",
    )
    p_dump.set_defaults(action=cmd_dump)
    p_dump.add_argument(
        "name", metavar="NAME", help="database to dump (all, known, ...)"
    )
    p_dump.add_argument(
        "--freq", action="store_true", help="include frequency as known to MorphMan"
    )

    p_count = subparsers.add_parser(
        "count",
        help="count morphemes in a corpus",
        description="Count all morphemes in the given files and emit a frequency table.",
    )
    p_count.set_defaults(action=cmd_count)
    p_count.add_argument(
        "files", nargs="*", metavar="FILE", help="input files of text to morphemize"
    )
    p_count.add_argument(
        "--mizer",
        default="mecab",
        choices=list(MIZERS.keys()),
        metavar="NAME",
        help="how to split morphemes (%s) (default %s)"  # pylint:disable=consider-using-f-string
        % (", ".join(list(MIZERS.keys())), "mecab"),
    )

    args = parser.parse_args()
    global CLI_PROFILE_PATH  # pylint:disable=global-statement
    if args.profile is not None:
        CLI_PROFILE_PATH = os.path.expanduser(os.path.normpath(args.profile))
    args.action(args)
