from interpreter import Eva_Interpreter
from test import auto_test
import ast
import sys

# Set Interpreter
Interpreter = Eva_Interpreter() 

mode = None
if len(sys.argv) == 2: mode = sys.argv[1]

if (mode=='-tests'):
    auto_test(Interpreter).tests()
elif (mode != None):
    read_file = open(sys.argv[1], "r")
    print(Interpreter.eval(ast.literal_eval(read_file.read().rstrip())))
    read_file.close()
else:
    while True:
        raw_string = input(">>> ")
        while ((raw_string.count("[") != raw_string.count("]")) and raw_string != ""): raw_string += input("... ")
        code = ast.literal_eval(raw_string)
        if type(code) == str:
            if code == "exit": break
        print(Interpreter.eval(code))