from dataclasses import dataclass


@dataclass
class RuleEntry:
    tag: str
    name: str
    name_adj: str
    condition: str