from utils import *
from classes.rule_entry import RuleEntry
import os

if __name__ == '__main__':
    rules_list = read_rules()
    print("Rules read successfully".ljust(100, '.'))
    tag_name_list = read_tag_names()
    tag_names = list(tag_name_list.items())
    print("Tag names read successfully".ljust(100, '.'))
    dynasty_names = read_dynasties()
    print("Dynasty names read successfully".ljust(100, '.'))

    rules: dict[str, list[RuleEntry]] = {}
    for rule in rules_list:
        for tag_name in tag_names:
            if rule.tags == [] or tag_name[0] in rule.tags:
                name = get_country_name(rule.name, tag_name)
                if name:
                    tag = get_tag_name(tag_name[0], rule.tag_name)
                    if tag == "TEO_ELECTORATE":
                        tag = "TEO_ELECTORATE_NAME" #for some reason it broke the name in the 'estates' tab
                    add_to_dict(rules, tag_name[0], RuleEntry(tag, name, ' '.join(rule.conditions)))
    
    dynasty_rules: list[tuple[str, str, str]] = []
    for rule in rules_list:
        if "{DYNASTY}" in rule.name:
            dynasty_rules.append((rule.name, ' '.join(rule.conditions), rule.tag_name))
    
    event_id = 1
    events: dict[str, str] = {}
    print("Creating event".ljust(100, '.'), end="\n", flush=True)
    event = ""
    event += "### generated events for dynamic names\n\n"
    event += "namespace = {event_name}\n\n".format(event_name=EVENT_NAME)
    event += "country_event = {\n"
    event += "\tid = {event_name}.0\n".format(event_name=EVENT_NAME)
    event += "\ttitle = {event_name}.0.title\n".format(event_name=EVENT_NAME)
    event += "\tdesc = {event_name}.0.desc\n".format(event_name=EVENT_NAME)
    event += "\tpicture = TRADEGOODS_eventPicture\n\n"
    event += "\thidden = yes\n"
    event += "\tis_triggered_only = yes\n\n"
    event += "\timmediate = {\n"
    for tag in tag_names:
        event += "\t\t"
        event += "if = { limit = { tag = "
        event += tag[0]
        event += " } "
        event += "country_event = { id = "
        event += "{event_name}.".format(event_name=EVENT_NAME)
        event += str(event_id)
        event += " } }\n"
        events[tag[0]] = str(event_id)
        event_id += 1
    for dynasty_rule in dynasty_rules:
        event += "\t\t"
        event += "if = { limit = { "
        event += str(dynasty_rule[1])
        event += " } " 
        event += "country_event = { id = "
        event += "{event_name}.".format(event_name=EVENT_NAME)
        event += str(event_id)
        event += " } }\n"
        events[dynasty_rule[0]] = str(event_id)
        event_id += 1
    event += "\t}\n"
    event += "\toption = {\n"
    event += "\t\tname = {event_name}.0.a\n".format(event_name=EVENT_NAME)
    event += "\t}\n"
    event += "}\n"
    print("Processing tag rules".ljust(100, '.'), end="\n", flush=True)
    for tag in tag_names:
        id = events[tag[0]]
        event += "country_event = {\n"
        event += "\tid = {event_name}.{id}\n".format(id=id, event_name=EVENT_NAME)
        event += "\ttitle = {event_name}.{id}.title\n".format(id=id, event_name=EVENT_NAME)
        event += "\tdesc = {event_name}.{id}.desc\n".format(id=id, event_name=EVENT_NAME)
        event += "\tpicture = TRADEGOODS_eventPicture\n\n"
        event += "\thidden = yes\n"
        event += "\tis_triggered_only = yes\n\n"
        event += "\ttrigger = {"
        event += " tag = "
        event += tag[0]
        event += " }\n\n"
        event += "\timmediate = {\n"
        rules_values = rules[tag[0]]
        first = True
        for rules_value in rules_values:
            print("EVENTID={EVENTID}....tag={tag}".format(EVENTID=id, tag=rules_value.tag).ljust(100, '.'), end="\r", flush=True)
            event += "\t\t"
            event += "if = { limit = { "
            event += str(rules_value.condition)
            event += " } override_country_name = "
            event += rules_value.tag
            event += " }\n"
        event += "\t}\n"
        event += "\toption = {\n"
        event += "\t\tname = {event_name}.{id}.a\n".format(id=id, event_name=EVENT_NAME)
        event += "\t}\n"
        event += "}\n"
    print()
    print("Processing dynasty rules".ljust(100, '.'), end="\n", flush=True)
    for dynasty_rule in dynasty_rules:
        id = events[dynasty_rule[0]]
        event += "country_event = {\n"
        event += "\tid = {event_name}.{id}\n".format(id=id, event_name=EVENT_NAME)
        event += "\ttitle = {event_name}.{id}.title\n".format(id=id, event_name=EVENT_NAME)
        event += "\tdesc = {event_name}.{id}.desc\n".format(id=id, event_name=EVENT_NAME)
        event += "\tpicture = TRADEGOODS_eventPicture\n\n"
        event += "\thidden = yes\n"
        event += "\tis_triggered_only = yes\n\n"
        event += "\timmediate = {\n"
        for dynasty_name in dynasty_names:
            print("EVENTID={EVENTID}....dynasty_name={dynasty_name}".format(EVENTID=id, dynasty_name=dynasty_name).ljust(100, '.'), end="\r", flush=True)
            event += "\t\t"
            event += "if = { limit = { dynasty = \""
            event += dynasty_name
            event += "\" } override_country_name = "
            event += dynasty_name.upper().replace(" ", "_").replace("-", "_").replace("'", "") + "_" + dynasty_rule[2]
            event += " }\n"
        event += "\t}\n"
        event += "\n\toption = {\n"
        event += "\t\tname = {event_name}.{id}.a\n".format(id=id, event_name=EVENT_NAME)
        event += "\t}\n"
        event += "}\n"

    if not os.path.exists("output/events"):
        os.makedirs("output/events")
    output_event_file = open("output/events/{event_name}_events.txt".format(event_name=EVENT_NAME), "w+")
    print("\nWriting event".ljust(100, '.'), end="", flush=True)
    output_event_file.write(event)
    output_event_file.close()

    print("\nCreating localisation".ljust(100, '.'), end="", flush=True)
    print("\nProcessing tags".ljust(100, '.'), end="\n", flush=True)
    loc = ""
    loc += "l_english:\n"
    loc += "\n #tag rules\n\n"
    for rule in rules.items():
        loc += " #"
        loc += rule[0]
        loc += "\n"
        for name in rule[1]:
            print("tag={tag}".format(tag=name.tag).ljust(100, '.'), end="\r", flush=True)
            loc += " "
            loc += name.tag
            loc += ": \""
            loc += name.name
            loc += "\"\n "
            loc += name.tag + "_ADJ: \""
            loc += tag_name_list[rule[0]].adj
            loc += "\"\n"
            if (tag_name_list[rule[0]].adj2 != None):
                loc += name.tag + "_ADJ2: \""
                loc += tag_name_list[rule[0]].adj2
                loc += "\"\n"
    loc += " #dynasties\n"
    print("\nProcessing dynasties".ljust(100, '.'), end="\n", flush=True)
    for dynasty_rule in dynasty_rules:
        loc += "\n #"
        loc += dynasty_rule[2]
        loc += "\n"
        for dynasty_name in dynasty_names:
            print("dynasty_name={dynasty_name}".format(dynasty_name=dynasty_name).ljust(100, '.'), end="\r", flush=True)
            loc += " "
            loc += dynasty_name.upper().replace(" ", "_").replace("-", "_").replace("'", "") + "_" + dynasty_rule[2]
            loc += ": \""
            loc += dynasty_rule[0].replace("{DYNASTY}", dynasty_name.title())
            loc += "\"\n "
            loc += dynasty_name.upper().replace(" ", "_").replace("-", "_").replace("'", "") + "_" + dynasty_rule[2] + "_ADJ: \""
            loc += dynasty_name.title()
            loc += "\"\n"

    loc += "update_dynamic_names_decision_title: \"Update Dynamic Names\"\n"
    loc += "update_dynamic_names_decision_desc: \"Force update dynamic names (for example when you upgraded your government rank). By default it happens every 2 in-game years.\"\n"
    print("\nWriting localisation".ljust(100, '.'), flush=True)
    if not os.path.exists("output/localisation"):
        os.makedirs("output/localisation")
    localisation_file = open("output/localisation/{event_name}_localisation_l_english.yml".format(event_name=EVENT_NAME), "w+", encoding="utf-8-sig")
    localisation_file.write(loc)
    localisation_file.close()

    print("Creating on_actions".ljust(100, '.')) 
    on_actions = "on_startup = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_government_change = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_native_change_government = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_religion_change = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_primary_culture_changed = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_monarch_death = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_country_creation = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_bi_yearly_pulse = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"
    on_actions += "on_country_released = {\n"
    on_actions += "\tevents = { "
    on_actions += "{event_name}.0 ".format(event_name=EVENT_NAME)
    on_actions += "}\n}\n\n"

    print("Writing on_actions".ljust(100, '.'))
    if not os.path.exists("output/common/on_actions"):
            os.makedirs("output/common/on_actions")

    on_actions_file = open("output/common/on_actions/{event_name}_on_actions.txt".format(event_name=EVENT_NAME), "w+")
    on_actions_file.write(on_actions)
    on_actions_file.close()

    print("Creating decision".ljust(100, '.')) 
    decision = ""
    decision += "country_decisions = {\n"
    decision += "\tupdate_dynamic_names_decision = {\n"
    decision += "\t\tpotential = { always = yes }\n"
    decision += "\t\tallow = { always = yes }\n"
    decision += "\t\tai_will_do = { factor = 0 }\n"
    decision += "\t\teffect = {\n"
    decision += "\t\t\tcountry_event  = { id = "
    decision += "{event_name}.0 ".format(event_name=EVENT_NAME)
    decision += " }\n"
    decision += "\t\t}\n"
    decision += "\t}"
    decision += "}\n"

    print("Writing decision".ljust(100, '.'))
    if not os.path.exists("output/decisions"):
            os.makedirs("output/decisions")

    decision_file = open("output/decisions/{event_name}_decisions.txt".format(event_name=EVENT_NAME), "w+")
    decision_file.write(decision)
    decision_file.close()

    input("Mod creation successful. Press any key to close this window.")