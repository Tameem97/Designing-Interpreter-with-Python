from eva import Eva_Interpreter
from test import test


# Set Interpreter
Interpreter = Eva_Interpreter() 


# Self Evaluating Expression Test
test(Interpreter.eval(9), 9, "Self Evaluating Expression Failed")
test(Interpreter.eval(100), 100, "Self Evaluating Expression Failed")
test(Interpreter.eval("\"Tameem\""), "Tameem", "Self Evaluating Expression Failed")


# Math Operations Test
test(Interpreter.eval(["+", 90, 9]), 99, "Addition Expression Failed")
test(Interpreter.eval(["+", ["+", 7, 3], 90]), 100, "Addition Expression Failed")
test(Interpreter.eval(["+", ["-", 81, ["*", 9, 9]], 90]), 90, "Addition Expression Failed")


# Variables
test(Interpreter.eval(["var", "x", 9]), 9, "Variable Declaration Failed")
test(Interpreter.eval("x"), 9, "Variable Declaration Failed")
test(Interpreter.eval("True"), True, "Variable Declaration Failed")
test(Interpreter.eval(["var", "i", "True"]), True, "Variable Declaration Failed")
test(Interpreter.eval("i"), True, "Variable Declaration Failed")
test(Interpreter.eval(["var", "a", ["+", 9, 9]]), 18, "Variable Declaration Failed")


# Block
test(Interpreter.eval(['begin', 
                    ['var', 'x', 10],
                    ['var', 'y', 20],
                    ['+', ['*', 'x', 'y'], 30]]), 230, "Code Blocked Failed")


# Separate Environment
test(Interpreter.eval(['begin', 
                     ['var', 'x', 10],
                     ['begin', 
                        ['var', 'x', 20], 'x' ],
                    'x']), 10, "Block Failed")


# Outer Environment Variable Access
test(Interpreter.eval(['begin', 
                     ['var', 'value', 10],
                     ['var', 'result', ['begin', 
                        ['var', 'x', ['+', 'value', 10]], 'x' ]],
                    'result']), 20, "Variable Access Error")


# Variable Assignment
test(Interpreter.eval(['begin', 
                     ['var', 'data', 10],
                     ['begin', 
                        ['set', 'data', 100]], 'data']), 100, "Variable Assignment Failed")


# If Condition
test(Interpreter.eval(['begin', 
                     ['var', 'x', 0],
                     ['var', 'y', 0], 
                        ['if', ['>', 'x', 10],
                          ['set', 'y', 20], 
                          ['set', 'y', 30],
                          ],
                          'y']), 30, "If block Failed")



# If Condition
test(Interpreter.eval(['begin', 
                     ['var', 'x', 0],
                     ['var', 'y', 0], 
                        ['if', ['>', 'x', 10],
                          ['set', 'y', 20], 
                          ['set', 'y', 30],
                          ],
                          'y']), 30, "If block Failed")



# while loop
test(Interpreter.eval(['begin', 
                     ['var', 'c', 0],
                     ['var', 'r', 0], 
                        ['while', ['<', 'c', 10],
                         ['begin', 
                          ['set', 'r', ['+', 'r', 1]], 
                          ['set', 'c', ['+', 'c', 1]],
                          ]],
                          'r']), 10, "While Loop failed")


# Factorial
test(Interpreter.eval(['begin', 
                     ['var', 'fact', 9],
                     ['var', 'result', 1], 
                        ['while', ['>=', 'fact', 1],
                         ['begin', 
                          ['set', 'result', ['*', 'result', 'fact']], 
                          ['set', 'fact', ['-', 'fact', 1]],
                          ]],
                          'result']), 362880, "Factorial failed")