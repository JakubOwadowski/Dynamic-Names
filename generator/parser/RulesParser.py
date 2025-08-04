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
        4,1,11,71,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,1,0,4,
        0,14,8,0,11,0,12,0,15,1,0,1,0,1,1,1,1,1,1,1,1,1,1,3,1,25,8,1,1,1,
        3,1,28,8,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,3,1,3,4,3,40,8,3,11,
        3,12,3,41,1,3,1,3,1,4,1,4,1,4,1,4,4,4,50,8,4,11,4,12,4,51,1,4,1,
        4,1,5,1,5,1,5,1,5,4,5,60,8,5,11,5,12,5,61,1,5,1,5,1,5,1,5,1,5,3,
        5,69,8,5,1,5,0,0,6,0,2,4,6,8,10,0,0,73,0,13,1,0,0,0,2,19,1,0,0,0,
        4,31,1,0,0,0,6,35,1,0,0,0,8,45,1,0,0,0,10,55,1,0,0,0,12,14,3,2,1,
        0,13,12,1,0,0,0,14,15,1,0,0,0,15,13,1,0,0,0,15,16,1,0,0,0,16,17,
        1,0,0,0,17,18,5,0,0,1,18,1,1,0,0,0,19,20,5,7,0,0,20,21,5,1,0,0,21,
        22,5,2,0,0,22,24,3,4,2,0,23,25,3,6,3,0,24,23,1,0,0,0,24,25,1,0,0,
        0,25,27,1,0,0,0,26,28,3,8,4,0,27,26,1,0,0,0,27,28,1,0,0,0,28,29,
        1,0,0,0,29,30,5,3,0,0,30,3,1,0,0,0,31,32,5,4,0,0,32,33,5,1,0,0,33,
        34,5,8,0,0,34,5,1,0,0,0,35,36,5,5,0,0,36,37,5,1,0,0,37,39,5,2,0,
        0,38,40,5,7,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,
        1,0,0,0,42,43,1,0,0,0,43,44,5,3,0,0,44,7,1,0,0,0,45,46,5,6,0,0,46,
        47,5,1,0,0,47,49,5,2,0,0,48,50,3,10,5,0,49,48,1,0,0,0,50,51,1,0,
        0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,3,0,0,54,9,
        1,0,0,0,55,56,5,7,0,0,56,68,5,1,0,0,57,59,5,2,0,0,58,60,3,10,5,0,
        59,58,1,0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,63,1,
        0,0,0,63,64,5,3,0,0,64,69,1,0,0,0,65,69,5,7,0,0,66,69,5,8,0,0,67,
        69,5,9,0,0,68,57,1,0,0,0,68,65,1,0,0,0,68,66,1,0,0,0,68,67,1,0,0,
        0,69,11,1,0,0,0,7,15,24,27,41,51,61,68
    ]

class RulesParser ( Parser ):

    grammarFileName = "Rules.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'{'", "'}'", "'name'", "'tags'", 
                     "'conditions'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "IDENTIFIER", 
                      "STRING", "NUMBER", "WS", "COMMENT" ]

    RULE_root = 0
    RULE_ruleObject = 1
    RULE_nameBlock = 2
    RULE_tagsBlock = 3
    RULE_conditionsBlock = 4
    RULE_expr = 5

    ruleNames =  [ "root", "ruleObject", "nameBlock", "tagsBlock", "conditionsBlock", 
                   "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    IDENTIFIER=7
    STRING=8
    NUMBER=9
    WS=10
    COMMENT=11

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
            self.state = 13 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.ruleObject()
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 17
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
            self.state = 19
            self.match(RulesParser.IDENTIFIER)
            self.state = 20
            self.match(RulesParser.T__0)
            self.state = 21
            self.match(RulesParser.T__1)
            self.state = 22
            self.nameBlock()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 23
                self.tagsBlock()


            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==6:
                self.state = 26
                self.conditionsBlock()


            self.state = 29
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
            self.state = 31
            self.match(RulesParser.T__3)
            self.state = 32
            self.match(RulesParser.T__0)
            self.state = 33
            localctx.name = self.match(RulesParser.STRING)
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
        self.enterRule(localctx, 6, self.RULE_tagsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(RulesParser.T__4)
            self.state = 36
            self.match(RulesParser.T__0)
            self.state = 37
            self.match(RulesParser.T__1)
            self.state = 39 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 38
                localctx.tag = self.match(RulesParser.IDENTIFIER)
                self.state = 41 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 43
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
        self.enterRule(localctx, 8, self.RULE_conditionsBlock)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self.match(RulesParser.T__5)
            self.state = 46
            self.match(RulesParser.T__0)
            self.state = 47
            self.match(RulesParser.T__1)
            self.state = 49 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                localctx.condition = self.expr()
                self.state = 51 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==7):
                    break

            self.state = 53
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
            self.id_ = None # Token
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
        self.enterRule(localctx, 10, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            localctx.id_ = self.match(RulesParser.IDENTIFIER)
            self.state = 56
            self.match(RulesParser.T__0)
            self.state = 68
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.state = 57
                localctx.value = self.match(RulesParser.T__1)
                self.state = 59 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 58
                    self.expr()
                    self.state = 61 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==7):
                        break

                self.state = 63
                self.match(RulesParser.T__2)
                pass
            elif token in [7]:
                self.state = 65
                self.match(RulesParser.IDENTIFIER)
                pass
            elif token in [8]:
                self.state = 66
                self.match(RulesParser.STRING)
                pass
            elif token in [9]:
                self.state = 67
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





