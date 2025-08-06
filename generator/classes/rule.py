from dataclasses import dataclass, field
from typing import List


@dataclass
class Rule:
    name: str
    id: str
    tags: List[str] = field(default_factory=list)
    conditions: List[str] = field(default_factory=list)
    revolutionary: bool = False
