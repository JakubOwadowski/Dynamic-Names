from parser.RulesBuilder import RulesBuilder
from parser.RulesLexer import RulesLexer
from parser.RulesParser import RulesParser

from antlr4 import *
from classes.Localisation import Localisation
from classes.Rule import Rule
from defines.defines import *

# -----------------
# Utility Functions
# -----------------


def process_name(name: str) -> str:
    return name.replace('"', "").replace("\n", "").strip()


def get_tag_name(tag: str, tag_name: str) -> str:
    return tag + "_" + tag_name


def split_stripped(s: str, sep: str = ",", maxsplit: int = -1) -> list[str]:
    return [part.strip() for part in s.split(sep, maxsplit)]


def read_lines(path: str):
    with open(path, encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            yield line


def get_country_name(rule_name: str, tag_name: tuple[str, Localisation]) -> str:
    if "NAME_ADJ2" in rule_name:
        rule_name = rule_name.replace("{NAME_ADJ2}", tag_name[1].adj2)
    elif "NAME_ADJ" in rule_name:
        rule_name = rule_name.replace("{NAME_ADJ}", tag_name[1].adj)
    elif "NAME" in rule_name:
        rule_name = rule_name.replace("{NAME}", tag_name[1].name)
    elif "DYNASTY" not in rule_name:
        rule_name = rule_name
    else:
        rule_name = None
    return rule_name


def get_dynasty_name(rule_name: str, dynasty_name: str) -> str:
    if "DYNASTY" in rule_name:
        rule_name = rule_name.replace("{DYNASTY}", dynasty_name.capitalize())
    else:
        rule_name = None
    return rule_name


# ------------------------------------
# Extraction / Rule-Building Functions
# ------------------------------------


def read_rules() -> list[Rule]:
    input_stream = FileStream(RULES_PATH, encoding="utf-8-sig")
    lexer = RulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RulesParser(token_stream)
    tree = parser.root()

    visitor = RulesBuilder()
    return visitor.visit(tree)


def read_tag_names(file_path: str) -> dict[str, Localisation]:
    tag_names = read_lines(file_path)
    tag_name_list: dict[str, Localisation] = {}
    for line in tag_names:
        line_split = line.split(":")
        name = line_split[0]
        value = line_split[1]
        if "_ADJ2" in name:
            key = name.replace("_ADJ2", "")
            tagName = tag_name_list[key]
            tagName.adj = process_name(value)
        elif "_ADJ" in name:
            key = name.replace("_ADJ", "")
            tagName = tag_name_list[key]
            tagName.adj = process_name(value)
        else:
            value = process_name(value)
            tagName = Localisation(name=value, adj=None, adj2=None)
            tag_name_list[name] = tagName
    return tag_name_list


def read_dynasties() -> list[str]:
    dynasty_names = read_lines(DYNASTIES_PATH)
    dynasty_names_list = []
    for dynasty in dynasty_names:
        dynasty_names_list.append(dynasty.replace("\n", ""))
    return dynasty_names_list


def add_revolutionaries():
    return [
        Rule(
            name=loc.name,
            name_adj=loc.adj,
            id=f"REV_{tag}",
            tags=[tag],
            conditions=[
                "government = republic",
                "is_revolutionary_republic_trigger = yes",
            ],
        )
        for tag, loc in read_tag_names(REVOLUTIONARIES_PATH).items()
    ]


def add_subject_rules(file_path, id_prefix, overlord_condition):
    # Detect scope variable
    def get_scope(key):
        if key.endswith("_superregion"):
            return "superregion"
        elif key.endswith("_region"):
            return "region"
        elif key.endswith("_area"):
            return "area"
        else:
            raise ValueError(f"Unknown scope type for key: {key}")

    rules = []
    for line in read_lines(file_path):
        key, name = split_stripped(line)

        rules.append(
            Rule(
                name=name,
                id=f"{id_prefix}_{key.upper()}",
                conditions=[
                    "OR = { is_subject_of_type = vassal is_subject_of_type = march }",
                    f"overlord = {{ {overlord_condition} }}"
                    f"capital_scope = {{ {get_scope(key)} = {key} }}",
                ],
            )
        )
    return rules


# Feudatories for each area in China
def add_feudatories():
    return add_subject_rules(
        file_path="data/feudatories.txt",
        id_prefix="FEUD",
        overlord_condition="is_emperor_of_china = yes",
    )


# Tang-style Chinese protectorates for each region surrounding China
def add_protectorates():
    return add_subject_rules(
        file_path="data/protectorates.txt",
        id_prefix="PROT",
        overlord_condition="is_emperor_of_china = yes",
    )


# Japanese puppet states
def add_jap_puppets():
    return add_subject_rules(
        file_path="data/japanese_puppets.txt",
        id_prefix="JAP_PUPPET",
        overlord_condition="tag = JAP",
    )


# Adds different names for the Emperor of China based on their primary culture
def add_emperor_of_china():
    return [
        Rule(
            name=name,
            id=f"GREAT_{culture.upper()}",
            conditions=[
                "is_emperor_of_china = yes",
                f"primary_culture = {culture}",
            ],
        )
        for culture, name in (
            split_stripped(line)
            for line in read_lines("data/empire_of_china_names.txt")
        )
    ]


# Changes the name of Korea based on the current ruling clan
def add_korean_dynasties():
    rules = []
    rule_templates = [
        (
            "Kingdom of {name}",
            "{id}_K",
            [
                "has_reform = monarchy_mechanic",
                "government_rank = 2",
                "NOT = { government_rank = 3 }",
            ],
        ),
        (
            "Empire of {name}",
            "{id}_E",
            [
                "has_reform = monarchy_mechanic",
                "government_rank = 3",
            ],
        ),
        (
            "Republic of {name}",
            "{id}_R",
            [
                "government = republic",
            ],
        ),
        (
            "Great {name}",
            "{id}_EOC",
            [
                "is_emperor_of_china = yes",
                "primary_culture = korean",
            ],
        ),
    ]

    for line in read_lines(KOREAN_DYNASTIES_PATH):
        dynasty, name, name_adj = split_stripped(line)
        for title, id_template, extra_conditions in rule_templates:
            rule = Rule(
                name=title.format(name=name),
                name_adj=name_adj,
                id=id_template.format(id=name.upper()),
                tags=["KOR"],
                conditions=extra_conditions + [f'dynasty = "{dynasty}"'],
            )
            rules.append(rule)
    return rules


# Add Eyalets of The Ottoman Empire
def add_eyalets():
    rules = []
    n = 0
    for line in read_lines(EYALETS_PATH):
        name, tags = split_stripped(line, maxsplit=1)
        rule = Rule(
            name=f"Eyalet-i {name}",
            id=f"EY{n}",
            tags=tags.split(","),
            conditions=[
                "OR = { "
                + " ".join(
                    [
                        "is_subject_of_type = eyalet",
                        "is_subject_of_type = core_eyalet",
                        "has_reform = barbary_eyalet_government",
                        "has_reform = eyalet_government",
                    ]
                )
                + " }"
            ],
        )
        rules.append(rule)
        n += 1
    return rules
