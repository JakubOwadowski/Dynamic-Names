# Generated from Rules.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,80,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,27,
        8,1,1,1,3,1,30,8,1,1,1,3,1,33,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,4,4,49,8,4,11,4,12,4,50,1,4,1,4,1,5,1,
        5,1,5,1,5,4,5,59,8,5,11,5,12,5,60,1,5,1,5,1,6,1,6,1,6,1,6,4,6,69,
        8,6,11,6,12,6,70,1,6,1,6,1,6,1,6,1,6,3,6,78,8,6,1,6,0,0,7,0,2,4,
        6,8,10,12,0,0,82,0,15,1,0,0,0,2,21,1,0,0,0,4,36,1,0,0,0,6,40,1,0,
        0,0,8,44,1,0,0,0,10,54,1,0,0,0,12,64,1,0,0,0,14,16,3,2,1,0,15,14,
        1,0,0,0,16,17,1,0,0,0,17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,
        19,20,5,0,0,1,20,1,1,0,0,0,21,22,5,8,0,0,22,23,5,1,0,0,23,24,5,2,
        0,0,24,26,3,4,2,0,25,27,3,6,3,0,26,25,1,0,0,0,26,27,1,0,0,0,27,29,
        1,0,0,0,28,30,3,8,4,0,29,28,1,0,0,0,29,30,1,0,0,0,30,32,1,0,0,0,
        31,33,3,10,5,0,32,31,1,0,0,0,32,33,1,0,0,0,33,34,1,0,0,0,34,35,5,
        3,0,0,35,3,1,0,0,0,36,37,5,4,0,0,37,38,5,1,0,0,38,39,5,9,0,0,39,
        5,1,0,0,0,40,41,5,5,0,0,41,42,5,1,0,0,42,43,5,9,0,0,43,7,1,0,0,0,
        44,45,5,6,0,0,45,46,5,1,0,0,46,48,5,2,0,0,47,49,5,8,0,0,48,47,1,
        0,0,0,49,50,1,0,0,0,50,48,1,0,0,0,50,51,1,0,0,0,51,52,1,0,0,0,52,
        53,5,3,0,0,53,9,1,0,0,0,54,55,5,7,0,0,55,56,5,1,0,0,56,58,5,2,0,
        0,57,59,3,12,6,0,58,57,1,0,0,0,59,60,1,0,0,0,60,58,1,0,0,0,60,61,
        1,0,0,0,61,62,1,0,0,0,62,63,5,3,0,0,63,11,1,0,0,0,64,65,5,8,0,0,
        65,77,5,1,0,0,66,68,5,2,0,0,67,69,3,12,6,0,68,67,1,0,0,0,69,70,1,
        0,0,0,70,68,1,0,0,0,70,71,1,0,0,0,71,72,1,0,0,0,72,73,5,3,0,0,73,
        78,1,0,0,0,74,78,5,8,0,0,75,78,5,9,0,0,76,78,5,10,0,0,77,66,1,0,
        0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,13,1,0,0,0,8,17,
        26,29,32,50,60,70,77
    ]

class RulesParser ( Parser ):

    grammarFileName = "Rules.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'{'", "'}'", "'name'", "'name_adj'", 
                     "'tags'", "'conditions'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "IDENTIFIER", "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_ruleObject = 1
    RULE_nameBlock = 2
    RULE_nameAdjBlock = 3
    RULE_tagsBlock = 4
    RULE_conditionsBlock = 5
    RULE_expr = 6

    ruleNames =  [ "root", "ruleObject", "nameBlock", "nameAdjBlock", "tagsBlock", 
                   "conditionsBlock", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    IDENTIFIER=8
    STRING=9
    NUMBER=10
    WS=11
    COMMENT=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class RootContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(RulesParser.EOF, 0)

        def ruleObject(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulesParser.RuleObjectContext)
            else:
                return self.getTypedRuleContext(RulesParser.RuleObjectContext,i)


        def getRuleIndex(self):
            return RulesParser.RULE_root

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRoot" ):
                listener.enterRoot(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRoot" ):
                listener.exitRoot(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRoot" ):
                return visitor.visitRoot(self)
            else:
                return visitor.visitChildren(self)




    def root(self):

        localctx = RulesParser.RootContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_root)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.ruleObject()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 19
            self.match(RulesParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RuleObjectContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(RulesParser.IDENTIFIER, 0)

        def nameBlock(self):
            return self.getTypedRuleContext(RulesParser.NameBlockContext,0)


        def nameAdjBlock(self):
            return self.getTypedRuleContext(RulesParser.NameAdjBlockContext,0)


        def tagsBlock(self):
            return self.getTypedRuleContext(RulesParser.TagsBlockContext,0)


        def conditionsBlock(self):
            return self.getTypedRuleContext(RulesParser.ConditionsBlockContext,0)


        def getRuleIndex(self):
            return RulesParser.RULE_ruleObject

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRuleObject" ):
                listener.enterRuleObject(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRuleObject" ):
                listener.exitRuleObject(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRuleObject" ):
                return visitor.visitRuleObject(self)
            else:
                return visitor.visitChildren(self)




    def ruleObject(self):

        localctx = RulesParser.RuleObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_ruleObject)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self.match(RulesParser.IDENTIFIER)
            self.state = 22
            self.match(RulesParser.T__0)
            self.state = 23
            self.match(RulesParser.T__1)
            self.state = 24
            self.nameBlock()
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 25
                self.nameAdjBlock()


            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 28
                self.tagsBlock()


            self.state = 32
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 31
                self.conditionsBlock()


            self.state = 34
            self.match(RulesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def STRING(self):
            return self.getToken(RulesParser.STRING, 0)

        def getRuleIndex(self):
            return RulesParser.RULE_nameBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameBlock" ):
                listener.enterNameBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameBlock" ):
                listener.exitNameBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameBlock" ):
                return visitor.visitNameBlock(self)
            else:
                return visitor.visitChildren(self)




    def nameBlock(self):

        localctx = RulesParser.NameBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_nameBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(RulesParser.T__3)
            self.state = 37
            self.match(RulesParser.T__0)
            self.state = 38
            localctx.name = self.match(RulesParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameAdjBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name_adj = None # Token

        def STRING(self):
            return self.getToken(RulesParser.STRING, 0)

        def getRuleIndex(self):
            return RulesParser.RULE_nameAdjBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNameAdjBlock" ):
                listener.enterNameAdjBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNameAdjBlock" ):
                listener.exitNameAdjBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameAdjBlock" ):
                return visitor.visitNameAdjBlock(self)
            else:
                return visitor.visitChildren(self)




    def nameAdjBlock(self):

        localctx = RulesParser.NameAdjBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nameAdjBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(RulesParser.T__4)
            self.state = 41
            self.match(RulesParser.T__0)
            self.state = 42
            localctx.name_adj = self.match(RulesParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TagsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.tag = None # Token

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(RulesParser.IDENTIFIER)
            else:
                return self.getToken(RulesParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return RulesParser.RULE_tagsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTagsBlock" ):
                listener.enterTagsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTagsBlock" ):
                listener.exitTagsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTagsBlock" ):
                return visitor.visitTagsBlock(self)
            else:
                return visitor.visitChildren(self)




    def tagsBlock(self):

        localctx = RulesParser.TagsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_tagsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(RulesParser.T__5)
            self.state = 45
            self.match(RulesParser.T__0)
            self.state = 46
            self.match(RulesParser.T__1)
            self.state = 48 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 47
                localctx.tag = self.match(RulesParser.IDENTIFIER)
                self.state = 50 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 52
            self.match(RulesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionsBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.condition = None # ExprContext

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(RulesParser.ExprContext,i)


        def getRuleIndex(self):
            return RulesParser.RULE_conditionsBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionsBlock" ):
                listener.enterConditionsBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionsBlock" ):
                listener.exitConditionsBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionsBlock" ):
                return visitor.visitConditionsBlock(self)
            else:
                return visitor.visitChildren(self)




    def conditionsBlock(self):

        localctx = RulesParser.ConditionsBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_conditionsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(RulesParser.T__6)
            self.state = 55
            self.match(RulesParser.T__0)
            self.state = 56
            self.match(RulesParser.T__1)
            self.state = 58 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 57
                localctx.condition = self.expr()
                self.state = 60 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==8):
                    break

            self.state = 62
            self.match(RulesParser.T__2)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.identifier = None # Token
            self.value = None # Token

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(RulesParser.IDENTIFIER)
            else:
                return self.getToken(RulesParser.IDENTIFIER, i)

        def STRING(self):
            return self.getToken(RulesParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(RulesParser.NUMBER, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(RulesParser.ExprContext)
            else:
                return self.getTypedRuleContext(RulesParser.ExprContext,i)


        def getRuleIndex(self):
            return RulesParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = RulesParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 64
            localctx.identifier = self.match(RulesParser.IDENTIFIER)
            self.state = 65
            self.match(RulesParser.T__0)
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 66
                localctx.value = self.match(RulesParser.T__1)
                self.state = 68 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 67
                    self.expr()
                    self.state = 70 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==8):
                        break

                self.state = 72
                self.match(RulesParser.T__2)
                pass
            elif token in [8]:
                self.state = 74
                self.match(RulesParser.IDENTIFIER)
                pass
            elif token in [9]:
                self.state = 75
                self.match(RulesParser.STRING)
                pass
            elif token in [10]:
                self.state = 76
                self.match(RulesParser.NUMBER)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





