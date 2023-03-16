from eva import Eva_Interpreter
from test import auto_test


# Set Interpreter
Interpreter = Eva_Interpreter() 

auto_test(Interpreter, print_on=True, assert_on=True).tests()

