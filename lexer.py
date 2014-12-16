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






class Lexer:
    
    def __init__(self, debug=True):
        self.debug = debug
        self.line_number = 0
        self.tokens = []
        self.curr_state = States.ROOT.name
        self.rules = {}
        print("Inside __init__ of Lexer");

 
    def begin(self, curr_state):
        pass
   
    def tokenize(self, tok_type, lexeme):
        pass

    def lex(self, input_stream):
        print("inside the method 'lex' in Lexer class")





if __name__ == '__main__':
    
    with open(sys.argv[1], 'r') as input_file:
        data = input_file.read()
    
    print(data)

    lexer = Lexer(True)
    lexer.lex(data)    

