from classes.Subjects import Subjects
from classes.Localisation import Localisation
from classes.Rule import Rule
from defines.defines import *

# -----------------
# Utility Functions
# -----------------


def process_name(name: str) -> str:
    return name.replace('"', "").replace("\n", "").strip()


def get_tag_name(tag: str, tag_name: str) -> str:
    return tag.replace('\ufeff', '') + "_" + tag_name.replace('\ufeff', '')


def format_as_tag(str: str):
    return str.upper().replace(" ", "_").replace("-", "_").replace("'", "")


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


def unscrew_text(string: str) -> str:
    if isinstance(string, str):
        return string.encode("latin1").decode("utf-8")
    return string

# ------------------------------------
# Extraction / Rule-Building Functions
# ------------------------------------


def read_rules(path: str) -> list[Rule]:
    import pyradox

    data = pyradox.txt.parse_file(
        path=path,
        game="EU4",
        path_relative_to_game=False,
    )

    rules = []
    for key, rule in data.items():
        new_rule = Rule(
                id=unscrew_text(key),
                name=unscrew_text(rule["name"]),
                name_adj=unscrew_text(rule["name_adj"]),
                tags=list(rule["tags"].values()) if rule["tags"] else [],
                conditions=(
                    [" ".join(map(str.strip, str(rule["conditions"]).split("\n")))]
                    if rule["conditions"]
                    else []
                ),
            )
        
        if "name_adj2" in rule and rule["name_adj2"]:
            new_rule.name_adj2 = unscrew_text(rule["name_adj2"])
        rules.append(new_rule)
    return rules


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