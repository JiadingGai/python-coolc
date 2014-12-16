import sys
import re

class Lexer:
    
    def __init__(self, debug=True):
        pass
 
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

