from eva import Eva_Interpreter
from test import test


Interpreter = Eva_Interpreter() 


# Self Evaluating Expression Test
test(Interpreter.eval(9), 9, "Self Evaluating Expression Failed")
test(Interpreter.eval(100), 100, "Self Evaluating Expression Failed")
test(Interpreter.eval("\"Tameem\""), "Tameem", "Self Evaluating Expression Failed")
