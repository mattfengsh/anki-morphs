import re
from typing import Any

from . import name_file_utils
from .ankimorphs_config import AnkiMorphsConfig
from .morpheme import Morpheme
from .morphemizers.morphemizer import Morphemizer

square_brackets_regex = re.compile(r"\[[^]]*]")
round_brackets_regex = re.compile(r"（[^）]*）")
slim_round_brackets_regexp = re.compile(r"\([^)]*\)")
non_alpha_regexp = re.compile(r"[-'\w]")
filter_regexp = re.compile(r"\d+")
hyphen_regex = re.compile(r"-")
space_regex = re.compile(r"\s+")


def get_processed_spacy_morphs(am_config: AnkiMorphsConfig, doc: Any, nlp) -> list[Morpheme]:
    # doc: spacy.tokens.Doc

    morphs: list[Morpheme] = []

    for w in doc:
        if not non_alpha_regexp.search(w.text):
            continue

        if filter_regexp.search(w.text):
            continue

        if am_config.preprocess_ignore_names_morphemizer:
            if w.pos == 96:  # PROPN
                continue
        if w.pos_ == "PUNCT" or (w.pos_ == "PROPN" and w.ent_type_ == "PERSON"):
            continue
        if (w.pos_ == "PROPN" and w.ent_type_ in ["NORP", "FAC", "ORG", "GPE", "LOC", "PRODUCT", "EVENT",
                                                  "WORK_OF_ART", "LAW"]):
            doc_t = nlp(w.text.lower())
            for x in doc_t:
                if x.pos_ == "PROPN":
                    continue
                else:
                    morphs.append(
                        Morpheme(
                            lemma=w.lemma_,
                            inflection=w.text,
                        )
                    )
        else:
            morphs.append(
                Morpheme(
                    lemma=w.lemma_,
                    inflection=w.text,
                )
            )

    if am_config.preprocess_ignore_names_textfile:
        morphs = remove_names_textfile(morphs)

    return morphs


def get_processed_morphemizer_morphs(
    morphemizer: Morphemizer, expression: str, am_config: AnkiMorphsConfig
) -> list[Morpheme]:
    morphs: list[Morpheme] = morphemizer.get_morphemes_from_expr(expression)

    if am_config.preprocess_ignore_names_morphemizer:
        morphs = remove_names_morphemizer(morphs)

    if am_config.preprocess_ignore_names_textfile:
        morphs = remove_names_textfile(morphs)

    return morphs


def get_processed_expression(am_config: AnkiMorphsConfig, expression: str) -> str:
    if am_config.preprocess_ignore_bracket_contents:
        if square_brackets_regex.search(expression):
            expression = square_brackets_regex.sub("", expression)

    if am_config.preprocess_ignore_round_bracket_contents:
        if round_brackets_regex.search(expression):
            expression = round_brackets_regex.sub("", expression)

    if am_config.preprocess_ignore_slim_round_bracket_contents:
        if slim_round_brackets_regexp.search(expression):
            expression = slim_round_brackets_regexp.sub("", expression)

    if hyphen_regex.search(expression):
        expression = hyphen_regex.sub(" ", expression)

    return expression


def remove_names_morphemizer(morphs: list[Morpheme]) -> list[Morpheme]:
    return [morph for morph in morphs if not morph.is_proper_noun()]


def remove_names_textfile(morphs: list[Morpheme]) -> list[Morpheme]:
    names = name_file_utils.get_names_from_file()
    non_name_morphs: list[Morpheme] = []

    for morph in morphs:
        if morph.inflection not in names:
            non_name_morphs.append(morph)

    return non_name_morphs
