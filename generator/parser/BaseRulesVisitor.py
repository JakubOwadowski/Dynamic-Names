# Generated from Rules.g4 by ANTLR 4.13.2
from antlr4 import *

if "." in __name__:
    from .RulesParser import RulesParser
else:
    from RulesParser import RulesParser

# This class defines a complete generic visitor for a parse tree produced by RulesParser.


class BaseRulesVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by RulesParser#root.
    def visitRoot(self, ctx: RulesParser.RootContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RulesParser#ruleObject.
    def visitRuleObject(self, ctx: RulesParser.RuleObjectContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RulesParser#nameBlock.
    def visitNameBlock(self, ctx: RulesParser.NameBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RulesParser#tagsBlock.
    def visitTagsBlock(self, ctx: RulesParser.TagsBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RulesParser#conditionsBlock.
    def visitConditionsBlock(self, ctx: RulesParser.ConditionsBlockContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by RulesParser#expr.
    def visitExpr(self, ctx: RulesParser.ExprContext):
        return self.visitChildren(ctx)


del RulesParser
