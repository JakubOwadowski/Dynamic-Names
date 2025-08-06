from antlr4 import *

from classes.rule import Rule
from parser.BaseRulesVisitor import BaseRulesVisitor

if "." in __name__:
    from .RulesParser import RulesParser
else:
    from RulesParser import RulesParser


class RulesVisitor(BaseRulesVisitor):
    def visitRoot(self, ctx: RulesParser.RootContext):
        return [self.visit(rule) for rule in ctx.ruleObject()]

    def visitRuleObject(self, ctx: RulesParser.RuleObjectContext):
        tag_name = ctx.IDENTIFIER().getText()

        name = self.visit(ctx.nameBlock())
        tags = self.visit(ctx.tagsBlock()) if ctx.tagsBlock() else []
        conditions = self.visit(ctx.conditionsBlock()) if ctx.conditionsBlock() else []

        return Rule(name=name, id=tag_name, tags=tags, conditions=conditions)

    def visitNameBlock(self, ctx: RulesParser.NameBlockContext):
        return ctx.STRING().getText().strip('"')

    def visitTagsBlock(self, ctx: RulesParser.TagsBlockContext):
        return [id_.getText() for id_ in ctx.IDENTIFIER()]

    def visitConditionsBlock(self, ctx: RulesParser.ConditionsBlockContext):
        return [self.visit(expr) for expr in ctx.expr()]

    def visitExpr(self, ctx: RulesParser.ExprContext):
        identifiers = ctx.IDENTIFIER()
        key = identifiers[0].getText()

        if ctx.STRING():
            value = ctx.STRING().getText()
        elif ctx.NUMBER():
            value = ctx.NUMBER().getText()
        elif len(identifiers) == 2:
            value = identifiers[1].getText()
        elif ctx.expr():
            inner = " ".join(self.visit(e) for e in ctx.expr())
            value = f"{{ {inner} }}"
        else:
            raise ValueError("Unrecognized expression format")

        return f"{key} = {value}"


del RulesParser
