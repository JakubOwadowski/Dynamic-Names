
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

TAG_DEPENDANT_EVENT_TEMPLATE = """\
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

TAG_AGNOSTIC_EVENT_TEMPLATE = """\
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

FORMAT_TEMPLATES = ["{NAME}", "{NAME_ADJ}", "{NAME_ADJ2}", "{DYNASTY}"]