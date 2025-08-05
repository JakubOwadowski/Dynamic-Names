from dataclasses import dataclass


@dataclass
class RuleEntry:
    tag: str
    name: str
    condition: str
    revolutionary: bool = False
