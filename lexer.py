import sys
import re
from enum import Enum

class States(Enum):

    ROOT = 1
    COMMENT = 2
    SL_COMMENT = 3
    STRING = 4
    STRING_ERR = 5

class TokType(Enum):

    # Not sure about these
    THROWAWAY = -1
    WHITESPACE = 0
    NEWLINE = 1
    COMMENT = 3
    LPAREN = '('
    RPAREN = ')'
    LBRACKET = '{'
    RBRACKET = '}'
    AT = '@'
    SEMICOLON = ':'
    COLON = ';'
    MULT = '*'
    PLUS = '+'
    COMMA = ','
    DOT = '.'
    
    CLASS = 258
    ELSE = 259
    FI = 260
    IF = 261
    IN = 262
    INHERITS = 263
    LET = 264
    LOOP = 265
    POOL = 266
    THEN = 267
    WHILE = 268
    CASE = 269
    ESAC = 270
    OF = 271
    DARROW = 272
    NEW = 273
    ISVOID = 274
    STR_CONST = 275
    INT_CONST = 276
    BOOL_CONST = 277
    TYPEID = 278
    OBJECTID = 279
    ASSIGN = 280
    NOT = 281
    LE = 282
    ERROR = 283
    LET_STMT = 285


class Token:

    def __init__(self, token_type, lexeme):
        self.token_type = token_type;
        self.lexeme = lexeme


class Rule:
    """Reference: http://pygments.org/docs/lexerdevelopment/"""
    def __init__(self, tok_type, reg_expr, state = None, on_match = None):
        self.tok_type = tok_type
        self.reg_expr = reg_expr
        self.state = state
        self.on_match = on_match


class Lexer:
    
    def __init__(self, debug=True):
        self.debug = debug
        self.line_number = 0
        self.tokens = []
        self.curr_state = States.ROOT.name
        self.rules = {
            States.ROOT.name: [
                Rule(TokType.CLASS, r'(?i)class'),
                Rule(TokType.LET, r'(?i)let'),
                Rule(TokType.MULT, r'\n*')
            ],
            States.COMMENT.name: [
                Rule(TokType.COMMENT, r'\*\)', state = States.ROOT.name),
                Rule(TokType.NEWLINE, r'[\n]'),
                Rule(TokType.THROWAWAY, r'.')
            ],
            States.SL_COMMENT.name: [
                Rule(TokType.NEWLINE, r'[\n]', state = States.ROOT.name),
                Rule(TokType.COMMENT, r'--'),
                Rule(TokType.THROWAWAY, r'.') 
            ]
        }
        print("Inside __init__ of Lexer");

    def begin(self, curr_date):
        self.curr_state = curr_state
 
    def tokenize(self, tok_type, lexeme):
        self.tokens.append(Token(tok_type, lexeme))

    def lex(self, input_stream):
        print("inside the method 'lex' in Lexer class")
        input_ptr = 0
        while input_ptr < len(input_stream):
            match = None
            for rule in self.rules[self.curr_state ]:
                regex = re.compile(rule.reg_expr)
                match = regex.match(input_stream, input_ptr)
                if match:
                    if (rule.tok_type and
                        (rule.tok_type is not TokType.WHITESPACE and 
                         rule.tok_type is not TokType.THROWAWAY)
                       ):
                        self.tokenize(rule.tok_type, match.group(0))
                        if rule.tok_type == TokType.NEWLINE:
                            self.line_number += 1
      
                        if (self.debug and rule.tok_type != TokType.NEWLINE):
                            #TODO: Use rule.tok_type.name once all tokens are enumerated
                            print('{}{}'.format(self.line_number, ' ' + str(self.curr_state) + ' ' + str(rule.tok_type.name) + ' ' + '"' + match.group(0)) + '"')

                    if rule.state:
                        self.begin(rule.state)
                    break

            if not match:
                sys.stderr.write('Illegal character: %s\\n' % input_stream[input_ptr])
                sys.exit(1)
            else:
                input_ptr = match.end(0)

        return self.tokens




if __name__ == '__main__':
    
    with open(sys.argv[1], 'r') as input_file:
        data = input_file.read()
    
    print(data)

    lexer = Lexer(True)
    lexer.lex(data)    

