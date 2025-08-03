import json
from classes.rule import Rule
from classes.tagName import TagName
from defines.defines import *

def read_rules() -> list[Rule]:
    rules = open(RULES_PATH, encoding="utf-8-sig")
    rules_json = json.load(rules)
    rules_list = []

    for key, entry in rules_json.items():
        rule = Rule(entry["name"], key, entry["tags"], entry["conditions"])
        rules_list.append(rule)
    
    return rules_list

def read_tag_names() -> list[(str, TagName)]:
    tag_names = open(TAG_NAMES_PATH, encoding="utf-8-sig")
    tag_name_list: dict[str, TagName] = {}
    for line in tag_names:
        line_split = line.split(":")
        name = line_split[0]
        value = line_split[1]
        if ("_ADJ2" in name):
            key = name.replace("_ADJ2", "")
            tagName = tag_name_list[key]
            tagName.adj = process_name(value)
        elif ("_ADJ" in name):
            key = name.replace("_ADJ", "")
            tagName = tag_name_list[key]
            tagName.adj = process_name(value)
        else:
            value = process_name(value)
            tagName = TagName(name=value, adj=None, adj2=None)
            tag_name_list[name] = tagName
    return tag_name_list

def read_dynasties() -> list[str]:
    dynasty_names = open(DYNASTIES_PATH, encoding="utf-8-sig")
    dynasty_names_list = []
    for dynasty in dynasty_names:
        dynasty_names_list.append(dynasty.replace("\n", ""))
    return dynasty_names_list

def get_country_name(rule_name: str, tag_name: tuple[str, TagName]) -> str:
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
    return name.replace("\"", "").replace("\n", "").strip()

def get_tag_name(tag: str, tag_name: str) -> str:
    return tag + "_" + tag_name

def add_to_dict(dict: dict, key: str, value: str):
    if not key in dict.keys():
        dict[key] = []
    dict[key].append(value)
    return dict