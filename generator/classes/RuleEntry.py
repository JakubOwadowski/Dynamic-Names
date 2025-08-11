from dataclasses import dataclass


@dataclass
class RuleEntry:
    tag: str
    name: str
    name_adj: str
    name_adj2: str
    condition: str