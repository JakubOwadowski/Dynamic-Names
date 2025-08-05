#!/usr/bin/env python3

from utils import *
from classes.rule_entry import RuleEntry
import os
from collections import defaultdict


class ModBuilder:
    def __init__(self):
        # Read rules, tag names, and dynasty names from input files
        self.rules_list = read_rules()
        print("Rules read successfully")
        self.tag_name_list = read_tag_names()
        print("Tag names read successfully")
        self.dynasty_names = read_dynasties()
        print("Dynasty names read successfully")
        self.revolutionary_names_list = read_revolutionary_names()
        print("Revolutionary names read successfully")

        self.rules: dict[str, list[RuleEntry]] = defaultdict(list)
        self.tag_to_rules: dict[str, list[Rule]] = defaultdict(list)
        self.events = {}
        self.event_id = 1

        self.dynasty_keys = {
            name: name.upper().replace(" ", "_").replace("-", "_").replace("'", "")
            for name in self.dynasty_names
        }

    def assign_rules_to_tags(self):
        for tag, localisation in self.revolutionary_names_list.items():
            rule = Rule(
                name=localisation.name,
                tag_name=f"REV_{tag}",
                tags=[tag],
                conditions=[
                    "government = republic",
                    "is_revolutionary_republic_trigger = yes",
                ],
                revolutionary=True,
            )
            self.rules_list.append(rule)

        for rule in self.rules_list:
            if not rule.tags:
                for tag, _ in self.tag_name_list.items():
                    self.tag_to_rules[tag].append(rule)
            else:
                for tag in rule.tags:
                    self.tag_to_rules[tag].append(rule)

        for tag, _ in self.tag_name_list.items():
            for rule in self.tag_to_rules[tag]:
                name = get_country_name(rule.name, (tag, self.tag_name_list[tag]))
                if name:
                    tag_name_value = get_tag_name(tag, rule.tag_name)
                    if tag_name_value == "TEO_ELECTORATE":
                        tag_name_value = "TEO_ELECTORATE_NAME"
                    self.rules[tag].append(
                        RuleEntry(
                            tag_name_value,
                            name,
                            " ".join(rule.conditions),
                            revolutionary=rule.revolutionary,
                        )
                    )

    def generate_event_script(self):
        dynasty_rules = [
            (rule.name, " ".join(rule.conditions), rule.tag_name)
            for rule in self.rules_list
            if "{DYNASTY}" in rule.name
        ]

        # Compose event triggers for the initial event immediate block
        event_triggers = []
        for tag, _ in self.tag_name_list.items():
            event_triggers.append(
                f"        if = {{ limit = {{ tag = {tag} }} country_event = {{ id = {EVENT_NAME}.{self.event_id} }} }}"
            )
            self.events[tag] = str(self.event_id)
            self.event_id += 1

        for rule in dynasty_rules:
            event_triggers.append(
                f"        if = {{ limit = {{ {rule[1]} }} country_event = {{ id = {EVENT_NAME}.{self.event_id} }} }}"
            )
            self.events[rule[0]] = str(self.event_id)
            self.event_id += 1

        # Write event header with triggers
        event_lines = [
            EVENT_SCRIPT_HEADER.format(
                event_name=EVENT_NAME, event_triggers="\n".join(event_triggers)
            )
        ]

        # Country events per tag
        for tag, _ in self.tag_name_list.items():
            id = self.events[tag]
            conditions = []
            for rule in self.rules[tag]:
                conditions.append(
                    f"        if = {{ limit = {{ {rule.condition} }} override_country_name = {rule.tag} }}"
                )
            event_lines.append(
                COUNTRY_EVENT_TEMPLATE.format(
                    event_name=EVENT_NAME,
                    id=id,
                    tag=tag,
                    conditions="\n".join(conditions),
                )
            )

        # Dynasty rules events
        for rule in dynasty_rules:
            id = self.events[rule[0]]
            conditions = []
            for name in self.dynasty_names:
                key = self.dynasty_keys[name]
                conditions.append(
                    f'        if = {{ limit = {{ dynasty = "{name}" }} override_country_name = {key}_{rule[2]} }}'
                )
            event_lines.append(
                DYNASTY_EVENT_TEMPLATE.format(
                    event_name=EVENT_NAME, id=id, conditions="\n".join(conditions)
                )
            )

        os.makedirs("../events", exist_ok=True)
        with open(f"../events/{EVENT_NAME}_events.txt", "w+") as f:
            f.write("\n".join(event_lines))

        print("Writing event done")

    def generate_localisation(self):
        loc_lines = ["l_english:", "\n #tag rules\n"]
        for tag, entries in self.rules.items():
            loc_lines.append(f" # {tag}")
            for entry in entries:
                loc_lines.append(f' {entry.tag}: "{entry.name}"')
                if entry.revolutionary:
                    loc_lines.append(
                        f' {entry.tag}_REV: "{self.revolutionary_names_list[tag].adj}"'
                    )
                else:
                    loc_lines.append(
                        f' {entry.tag}_ADJ: "{self.tag_name_list[tag].adj}"'
                    )
                if self.tag_name_list[tag].adj2:
                    loc_lines.append(
                        f' {entry.tag}_ADJ2: "{self.tag_name_list[tag].adj2}"'
                    )

        loc_lines.append(" #dynasties")
        for rule in self.rules_list:
            if "{DYNASTY}" in rule.name:
                loc_lines.append(f"\n # {rule.tag_name}")
                for name in self.dynasty_names:
                    key = self.dynasty_keys[name]
                    loc_lines.append(
                        f' {key}_{rule.tag_name}: "{rule.name.replace("{DYNASTY}", name.title())}"'
                    )
                    loc_lines.append(f' {key}_{rule.tag_name}_ADJ: "{name.title()}"')

        loc_lines.append('update_dynamic_names_decision_title: "Update Dynamic Names"')
        loc_lines.append(
            'update_dynamic_names_decision_desc: "Force update dynamic names (e.g. after a government rank change). Happens automatically every 2 in-game years."'
        )

        os.makedirs("../localisation", exist_ok=True)
        with open(
            f"../localisation/{EVENT_NAME}_localisation_l_english.yml",
            "w+",
            encoding="utf-8-sig",
        ) as f:
            f.write("\n".join(loc_lines))

        print("Writing localisation done")

    def generate_on_actions(self):
        triggers = [
            "on_startup",
            "on_government_change",
            "on_native_change_government",
            "on_religion_change",
            "on_primary_culture_changed",
            "on_monarch_death",
            "on_country_creation",
            "on_bi_yearly_pulse",
            "on_country_released",
        ]

        on_actions_lines = [
            f"{trigger} = {{ events = {{ {EVENT_NAME}.0 }} }}" for trigger in triggers
        ]

        os.makedirs("../common/on_actions", exist_ok=True)
        with open(f"../common/on_actions/{EVENT_NAME}_on_actions.txt", "w+") as f:
            f.write("\n\n".join(on_actions_lines))

        print("Writing on_actions done")

    def generate_decision(self):
        os.makedirs("../decisions", exist_ok=True)
        with open(f"../decisions/{EVENT_NAME}_decisions.txt", "w+") as f:
            f.write(DECISION_TEMPLATE.format(event_name=EVENT_NAME))

        print("Writing decision done")

    def build(self):
        self.assign_rules_to_tags()
        self.generate_event_script()
        self.generate_localisation()
        self.generate_on_actions()
        self.generate_decision()


if __name__ == "__main__":
    builder = ModBuilder()
    builder.build()
