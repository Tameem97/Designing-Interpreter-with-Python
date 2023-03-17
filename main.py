from eva import Eva_Interpreter
from test import auto_test
import ast
import sys


# Set Interpreter
Interpreter = Eva_Interpreter() 

mode = None
if len(sys.argv)>1: mode = sys.argv[1]

if (mode=='-tests'):
    auto_test(Interpreter).tests()
else:
    while True:
        code = ast.literal_eval(input(">>> "))
        if type(code) == str:
            if code == "exit":
                break
        print(Interpreter.eval(code))


