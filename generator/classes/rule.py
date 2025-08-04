class Rule:
    def __init__(
        self, name: str, tag_name: str, tags: list[str], conditions: list[str]
    ):
        self.name = name
        self.tag_name = tag_name
        self.tags = tags
        self.conditions = conditions
