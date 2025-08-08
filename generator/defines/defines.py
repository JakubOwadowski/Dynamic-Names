RULES_PATH = "rules/rules.txt"
DYNASTIES_PATH = "data/dynasties.txt"
TAG_NAMES_PATH = "data/tag_names.txt"
REVOLUTIONARIES_PATH = "data/revolutionary_names.txt"
KOREAN_DYNASTIES_PATH = "data/korean_dynasties.txt"
JAPANESE_PUPPETS_PATH = "data/japanese_puppets.txt"
FEUDATORIES_PATH = "data/feudatories.txt"
PROTECTORATES_PATH = "data/protectorates.txt"
EYALETS_PATH = "data/eyalets.txt"
EMPIRE_OF_CHINA_NAMES = "data/empire_of_china_names.txt"

EVENT_NAME = "dynamic_names"

EVENT_SCRIPT_HEADER = """\
### generated events for dynamic names

namespace = {event_name}

country_event = {{
    id = {event_name}.0
    title = {event_name}.0.title
    desc = {event_name}.0.desc
    picture = TRADEGOODS_eventPicture
    hidden = yes
    is_triggered_only = yes

    immediate = {{
{event_triggers}
    }}

    option = {{
        name = {event_name}.0.a
    }}
}}
"""

COUNTRY_EVENT_TEMPLATE = """\
country_event = {{
    id = {event_name}.{id}
    title = {event_name}.{id}.title
    desc = {event_name}.{id}.desc
    picture = TRADEGOODS_eventPicture
    hidden = yes
    is_triggered_only = yes

    trigger = {{
        tag = {tag}
    }}

    immediate = {{
{conditions}
    }}

    option = {{
        name = {event_name}.{id}.a
    }}
}}
"""

DYNASTY_EVENT_TEMPLATE = """\
country_event = {{
    id = {event_name}.{id}
    title = {event_name}.{id}.title
    desc = {event_name}.{id}.desc
    picture = TRADEGOODS_eventPicture
    hidden = yes
    is_triggered_only = yes

    immediate = {{
{conditions}
    }}

    option = {{
        name = {event_name}.{id}.a
    }}
}}
"""

DECISION_TEMPLATE = """\
country_decisions = {{
    update_dynamic_names_decision = {{
        potential = {{ always = yes }}
        allow = {{ always = yes }}
        ai_will_do = {{ factor = 0 }}
        effect = {{ country_event = {{ id = {event_name}.0 }} }}
    }}
}}
"""
