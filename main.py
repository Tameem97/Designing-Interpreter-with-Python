from eva import Eva_Interpreter
from test import auto_test


# Set Interpreter
Interpreter = Eva_Interpreter() 

# Running tests

mode = 0

if (mode==0):
    auto_test(Interpreter, print_on=True, assert_on=True).tests()
else:
    # TODO
    ast = []
    code = input()
    print(code)


