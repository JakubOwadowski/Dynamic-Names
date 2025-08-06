# Generated from Rules.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .RulesParser import RulesParser
else:
    from RulesParser import RulesParser

# This class defines a complete listener for a parse tree produced by RulesParser.
class RulesListener(ParseTreeListener):

    # Enter a parse tree produced by RulesParser#root.
    def enterRoot(self, ctx:RulesParser.RootContext):
        pass

    # Exit a parse tree produced by RulesParser#root.
    def exitRoot(self, ctx:RulesParser.RootContext):
        pass


    # Enter a parse tree produced by RulesParser#ruleObject.
    def enterRuleObject(self, ctx:RulesParser.RuleObjectContext):
        pass

    # Exit a parse tree produced by RulesParser#ruleObject.
    def exitRuleObject(self, ctx:RulesParser.RuleObjectContext):
        pass


    # Enter a parse tree produced by RulesParser#nameBlock.
    def enterNameBlock(self, ctx:RulesParser.NameBlockContext):
        pass

    # Exit a parse tree produced by RulesParser#nameBlock.
    def exitNameBlock(self, ctx:RulesParser.NameBlockContext):
        pass


    # Enter a parse tree produced by RulesParser#nameAdjBlock.
    def enterNameAdjBlock(self, ctx:RulesParser.NameAdjBlockContext):
        pass

    # Exit a parse tree produced by RulesParser#nameAdjBlock.
    def exitNameAdjBlock(self, ctx:RulesParser.NameAdjBlockContext):
        pass


    # Enter a parse tree produced by RulesParser#tagsBlock.
    def enterTagsBlock(self, ctx:RulesParser.TagsBlockContext):
        pass

    # Exit a parse tree produced by RulesParser#tagsBlock.
    def exitTagsBlock(self, ctx:RulesParser.TagsBlockContext):
        pass


    # Enter a parse tree produced by RulesParser#conditionsBlock.
    def enterConditionsBlock(self, ctx:RulesParser.ConditionsBlockContext):
        pass

    # Exit a parse tree produced by RulesParser#conditionsBlock.
    def exitConditionsBlock(self, ctx:RulesParser.ConditionsBlockContext):
        pass


    # Enter a parse tree produced by RulesParser#expr.
    def enterExpr(self, ctx:RulesParser.ExprContext):
        pass

    # Exit a parse tree produced by RulesParser#expr.
    def exitExpr(self, ctx:RulesParser.ExprContext):
        pass



del RulesParser