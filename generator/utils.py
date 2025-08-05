from classes.rule import Rule
from classes.tagName import Localisation
from defines.defines import *
from antlr4 import *
from parser.RulesVisitor import RulesVisitor
from parser.RulesLexer import RulesLexer
from parser.RulesParser import RulesParser
from classes.rule import Rule
from defines.defines import *


def read_rules() -> list[Rule]:
    input_stream = FileStream(RULES_PATH, encoding="utf-8-sig")
    lexer = RulesLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = RulesParser(token_stream)
    tree = parser.root()

    visitor = RulesVisitor()
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
