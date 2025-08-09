#!/usr/bin/env python3

import os
from collections import defaultdict

from utils import *

from classes.RuleEntry import RuleEntry


class ModBuilder:
    def __init__(self):
        # Read rules, tag names, and dynasty names from input files
        self.rules_list = read_rules()
        print("Rules read successfully")
        self.tag_name_list = read_tag_names(TAG_NAMES_PATH)
        print("Tag names read successfully")
        self.dynasty_names = read_dynasties()
        print("Dynasty names read successfully")

        self.global_rules_list: list[Rule] = []
        self.rules: dict[str, list[RuleEntry]] = defaultdict(list)
        self.tag_to_rules: dict[str, list[Rule]] = defaultdict(list)
        self.events = {}
        self.event_id = 1

        self.dynasty_keys = {name: format_as_tag(name) for name in self.dynasty_names}

    def assign_rules(self):
        for module in [
            add_revolutionaries(),
            add_feudatories(),
            add_protectorates(),
            add_jap_puppets(),
            add_emperor_of_china(),
            add_shogunates(),
            add_eyalets(),
            add_dynastic_names(self.rules_list),
        ]:
            self.rules_list.extend(module)

        # Map rules to applicable tags
        for rule in self.rules_list:
            if not any(x in rule.name for x in FORMAT_TEMPLATES) and not rule.tags:
                self.global_rules_list.append(rule)
            else:
                target_tags = rule.tags or self.tag_name_list.keys()
                for tag in target_tags:
                    self.tag_to_rules[tag].append(rule)

        # Build final rule entries per tag
        for tag, loc in self.tag_name_list.items():
            for rule in self.tag_to_rules[tag]:
                name = get_country_name(rule.name, (tag, loc))
                if not name:
                    continue

                tag_name_value = get_tag_name(tag, rule.id)
                if tag_name_value == "TEO_ELECTORATE":
                    tag_name_value = "TEO_ELECTORATE_NAME"

                name_adj = rule.name_adj or loc.adj

                self.rules[tag].append(
                    RuleEntry(
                        tag=tag_name_value,
                        name=name,
                        name_adj=name_adj,
                        condition=" ".join(rule.conditions),
                    )
                )

    def generate_event_script(self):

        # Compose event triggers for the initial event immediate block
        event_triggers = []
        for tag, _ in self.tag_name_list.items():
            event_triggers.append(
                f"        if = {{ limit = {{ tag = {tag} }} country_event = {{ id = {EVENT_NAME}.{self.event_id} }} }}"
            )
            self.events[tag] = str(self.event_id)
            self.event_id += 1

        dynasty_rules = [rule for rule in self.rules_list if "{DYNASTY}" in rule.name]
        for rule in dynasty_rules:
            conditions = " ".join(rule.conditions)
            event_triggers.append(
                f"        if = {{ limit = {{ {conditions} }} country_event = {{ id = {EVENT_NAME}.{self.event_id} }} }}"
            )
            self.events[rule.name] = str(self.event_id)
            self.event_id += 1

        # Add global rules directly
        for rule in self.global_rules_list:
            conditions = " ".join(rule.conditions)
            event_triggers.append(
                f"        if = {{ limit = {{ {conditions} }} override_country_name = {rule.id} }}"
            )
            self.events[rule.name] = str(self.event_id)
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
                TAG_DEPENDANT_EVENT_TEMPLATE.format(
                    event_name=EVENT_NAME,
                    id=id,
                    tag=tag,
                    conditions="\n".join(conditions),
                )
            )

        # Dynasty rules events
        for rule in dynasty_rules:
            id = self.events[rule.name]
            conditions = []
            for name in self.dynasty_names:
                key = self.dynasty_keys[name]
                conditions.append(
                    f'        if = {{ limit = {{ dynasty = "{name}" }} override_country_name = {key}_{rule.id} }}'
                )
            event_lines.append(
                TAG_AGNOSTIC_EVENT_TEMPLATE.format(
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
                if entry.name_adj:
                    loc_lines.append(f' {entry.tag}_ADJ: "{entry.name_adj}"')

        loc_lines.append(" #dynasties")
        for rule in self.rules_list:
            if "{DYNASTY}" in rule.name:
                loc_lines.append(f"\n # {rule.id}")
                for name in self.dynasty_names:
                    key = self.dynasty_keys[name]
                    loc_lines.append(
                        f' {key}_{rule.id}: "{rule.name.replace("{DYNASTY}", name.title())}"'
                    )
                    loc_lines.append(f' {key}_{rule.id}_ADJ: "{name.title()}"')

        loc_lines.append(" #global rules")
        for rule in self.global_rules_list:
            loc_lines.append(f"\n # {rule.id}")
            loc_lines.append(f' {rule.id}: "{rule.name}"')
            if entry.name_adj:
                loc_lines.append(f' {rule.id}_ADJ: "{rule.name_adj}"')

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
        self.assign_rules()
        self.generate_event_script()
        self.generate_localisation()
        self.generate_on_actions()
        self.generate_decision()


if __name__ == "__main__":
    builder = ModBuilder()
    builder.build()
