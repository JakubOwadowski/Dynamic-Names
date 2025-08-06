from dataclasses import dataclass, field
from typing import List


@dataclass
class Rule:
    id: str
    name: str
    name_adj: str = None
    tags: List[str] = field(default_factory=list)
    conditions: List[str] = field(default_factory=list)