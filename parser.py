import sly
import lexer
from trees import Number, Symbol, List
from decimal import Decimal

class LispishParser(sly.Parser):
    tokens = lexer.LispishLexer.tokens

    @_("expression")
    def whole_program(self, p):
        return p.expression

    @_("NAME")
    def symbol(self, inTok):
        return Symbol(inTok.NAME)

    @_("NUMBER")
    def number(self, inTok):
        return Number(Decimal(inTok.NUMBER))

    @_("number")
    def expression(self, p):
        return p.number

    @_("symbol")
    def expression(self, p):
        return p.symbol

    @_("listy")
    def expression(self, p):
        return p.listy

    @_("LPAREN expression_list RPAREN")
    def listy(self, p):
        return List(p.expression_list)

    @_("expression")
    def expression_list(self, p):
        return [p.expression]

    @_("expression SEP expression_list")
    def expression_list(self, p):
        return [p.expression] + p.expression_list
        

if __name__ == "__main__":
    lex = lexer.LispishLexer()
    parser = LispishParser()

    while True:
        inp = input("--> ")
        tokens = lex.tokenize(inp)
        res = parser.parse(tokens)
        print(repr(res))
        print(res)
