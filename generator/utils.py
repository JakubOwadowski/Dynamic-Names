from parser.RulesLexer import RulesLexer
from parser.RulesParser import RulesParser
from parser.RulesBuilder import RulesBuilder

from antlr4 import *
from classes.Localisation import Localisation
from classes.Rule import Rule
from defines.defines import *


def read_rules() -> list[Rule]:
    input_stream = FileStream(RULES_PATH, encoding="utf-8-sig")
    lexer = RulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RulesParser(token_stream)
    tree = parser.root()

    visitor = RulesBuilder()
    return visitor.visit(tree)


def read_tag_names() -> dict[str, Localisation]:
    tag_names = open(TAG_NAMES_PATH, encoding="utf-8-sig")
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
    dynasty_names = open(DYNASTIES_PATH, encoding="utf-8-sig")
    dynasty_names_list = []
    for dynasty in dynasty_names:
        dynasty_names_list.append(dynasty.replace("\n", ""))
    return dynasty_names_list


def read_revolutionary_names() -> dict[str, Localisation]:
    revolutionary_names = open(REVOLUTIONARIES_PATH, encoding="utf-8-sig")
    revolutionary_names_list: dict[str, Localisation] = {}
    for line in revolutionary_names:
        if line.startswith("#") or not line.strip():
            continue
        line_split = line.split(":")
        name = line_split[0]
        value = line_split[1]
        if "_ADJ" in name:
            key = name.replace("_ADJ", "")
            tagName = revolutionary_names_list[key]
            tagName.adj = process_name(value)
        else:
            value = process_name(value)
            tagName = Localisation(name=value, adj=None, adj2=None)
            revolutionary_names_list[name] = tagName
    return revolutionary_names_list


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


def process_name(name: str) -> str:
    return name.replace('"', "").replace("\n", "").strip()


def get_tag_name(tag: str, tag_name: str) -> str:
    return tag + "_" + tag_name


def add_to_dict(dict: dict, key: str, value: str):
    if not key in dict.keys():
        dict[key] = []
    dict[key].append(value)
    return dict


# Feudatories for each area in China
def add_feudatories():
    with open("data/feudatories.txt", encoding="utf-8-sig") as f:
        rules = []
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            area, name = map(str.strip, line.split(",", 1))
            rule = Rule(
                name=name,
                id=f"FEUD_{area.upper()}",
                conditions=[
                    "OR = { is_subject_of_type = vassal is_subject_of_type = march }",
                    "overlord = { is_emperor_of_china = yes }",
                    f"capital_scope = {{ area = {area} }}",
                ],
            )
            rules.append(rule)
        return rules


# Tang-style Chinese protectorates for each region surrounding China
def add_protectorates():
    with open("data/protectorates.txt", encoding="utf-8-sig") as f:
        rules = []
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            region, name = map(str.strip, line.split(",", 1))
            rule = Rule(
                name=name,
                id=f"PROT_{region.upper()}",
                conditions=[
                    "OR = { is_subject_of_type = vassal is_subject_of_type = march }",
                    "overlord = { is_emperor_of_china = yes }",
                    f"capital_scope = {{ region = {region} }}",
                ],
            )
            rules.append(rule)
        return rules


# Japanese puppet states
def add_jap_puppets():
    with open("data/japanese_puppets.txt", encoding="utf-8-sig") as f:
        rules = []
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            region, name = map(str.strip, line.split(",", 1))
            if region == "china_superregion":
                variable = "superregion"
            else:
                variable = "region"
            rule = Rule(
                name=name,
                id=f"JAP_PUPPET_{region.upper()}",
                conditions=[
                    "OR = { is_subject_of_type = vassal is_subject_of_type = march }",
                    "overlord = { tag = JAP }",
                    f"capital_scope = {{ {variable} = {region} }}",
                ],
            )
            rules.append(rule)
        return rules


# Adds different names for the Emperor of China based on their primary culture
def add_emperor_of_china():
    with open("data/empire_of_china_names.txt", encoding="utf-8-sig") as f:
        rules = []
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            culture, name = map(str.strip, line.split(",", 1))
            rule = Rule(
                name=name,
                id=f"GREAT_{culture.upper()}",
                conditions=[
                    "is_emperor_of_china = yes",
                    f"primary_culture = {culture}",
                ],
            )
            rules.append(rule)
        return rules


# Changes the name of Korea based on the current ruling clan
def add_korean_dynasties():
    with open("data/korean_dynasties.txt", encoding="utf-8-sig") as f:
        rules = []
        rule_templates = [
            (
                "Kingdom of {name}",
                "{id}_K",
                [
                    "has_reform = monarchy_mechanic",
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

        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            dynasty, name, name_adj = map(str.strip, line.split(",", 2))
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
    with open("data/eyalets.txt", encoding="utf-8-sig") as f:
        rules = []
        n = 0
        for line in f:
            line = line.strip()
            if line.startswith("#") or not line:
                continue
            name, tags = map(str.strip, line.split(",", 1))
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
