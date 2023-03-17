from eva import Eva_Interpreter
from test import auto_test


# Set Interpreter
Interpreter = Eva_Interpreter() 

# Running tests

mode = 0

if (mode==0):
    auto_test(Interpreter, print_on=True, assert_on=True).tests()
elif mode == 1:
    # Running tests
    a = auto_test()
    a.test(Interpreter.eval(['begin', 
                                ['def', 'square', ["x", "y"], ["*", "y", "x"]],
                                ["square", 2, 9]]), 4, "Code Blocked Failed")
else:
    # TODO
    ast = []
    code = input()
    print(code)


