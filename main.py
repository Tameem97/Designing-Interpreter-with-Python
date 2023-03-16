from eva import Eva_Interpreter
from test import test


Interpreter = Eva_Interpreter() 


# Self Evaluating Expression Test
test(Interpreter.eval(9), 9, "Self Evaluating Expression Failed")
test(Interpreter.eval(100), 100, "Self Evaluating Expression Failed")
test(Interpreter.eval("\"Tameem\""), "Tameem", "Self Evaluating Expression Failed")


# Math Operations Test
test(Interpreter.eval(["+", 90, 9]), 99, "Addition Expression Failed")
test(Interpreter.eval(["+", ["+", 7, 3], 90]), 100, "Addition Expression Failed")
test(Interpreter.eval(["+", ["-", 81, ["*", 9, 9]], 90]), 90, "Addition Expression Failed")
