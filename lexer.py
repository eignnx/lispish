import sly

class LispishLexer(sly.Lexer):
    tokens = {
        LPAREN, RPAREN,
        NUMBER, NAME, SEP
    }

    LPAREN = r"\("
    RPAREN = r"\)"
    # including decimals
    NUMBER = r"-?((\.\d+)|(\d+\.\d*)|(\d+))"
    # get-values, +, - are valid names 
    NAME = r"[a-zA-Z_\-+*\/=<>][\w\-=><]*['!?]*"
    SEP = r"\s" # whitespace separator

if __name__ == "__main__":
    lex = LispishLexer()
    for tok in lex.tokenize(input("--> ")):
        print(tok)