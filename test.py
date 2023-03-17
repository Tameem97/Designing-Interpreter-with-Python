class auto_test:

    ctest = 0
    dtest = 0

    def __init__(self, Interpreter=None, print_on=True, assert_on= False) -> None:
        self.Interpreter = Interpreter
        self.print_on = print_on
        self.assert_on = assert_on


    def test(self, r, c, e):
        if (self.print_on == True):  print("Actual Result:", r, " Expected:", c)

        if (r==c): auto_test.ctest+=1 
        else: auto_test.dtest += 1

        if (self.assert_on): assert r == c, e


    def tests(self):
        # Self Evaluating Expression self.test
        self.test(self.Interpreter.eval(9), 9, "Self Evaluating Expression Failed")
        self.test(self.Interpreter.eval(100), 100, "Self Evaluating Expression Failed")
        self.test(self.Interpreter.eval("\"Tameem\""), "Tameem", "Self Evaluating Expression Failed")
        
        # Math Operations self.test
        self.test(self.Interpreter.eval(["+", 90, 9]), 99, "Addition Expression Failed")
        self.test(self.Interpreter.eval(["+", ["+", 7, 3], 90]), 100, "Addition Expression Failed")
        self.test(self.Interpreter.eval(["+", ["-", 81, ["*", 9, 9]], 90]), 90, "Addition Expression Failed")


        # Variables
        self.test(self.Interpreter.eval(["var", "x", 9]), 9, "Variable Declaration Failed")
        self.test(self.Interpreter.eval("x"), 9, "Variable Declaration Failed")
        self.test(self.Interpreter.eval("True"), True, "Variable Declaration Failed")
        self.test(self.Interpreter.eval(["var", "i", "True"]), True, "Variable Declaration Failed")
        self.test(self.Interpreter.eval("i"), True, "Variable Declaration Failed")
        self.test(self.Interpreter.eval(["var", "a", ["+", 9, 9]]), 18, "Variable Declaration Failed")


        # Block
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'x', 10],
                            ['var', 'y', 20],
                            ['+', ['*', 'x', 'y'], 30]]), 230, "Code Blocked Failed")


        # Separate Environment
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'x', 10],
                            ['begin', 
                                ['var', 'x', 20], 'x' ],
                            'x']), 10, "Block Failed")


        # Outer Environment Variable Access
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'value', 10],
                            ['var', 'result', ['begin', 
                                ['var', 'x', ['+', 'value', 10]], 'x' ]],
                            'result']), 20, "Variable Access Error")


        # Variable Assignment
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'data', 10],
                            ['begin', 
                                ['set', 'data', 100]], 'data']), 100, "Variable Assignment Failed")


        # If Condition
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'x', 0],
                            ['var', 'y', 0], 
                                ['if', ['>', 'x', 10],
                                ['set', 'y', 20], 
                                ['set', 'y', 30],
                                ],
                                'y']), 30, "If block Failed")



        # If Condition
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'x', 0],
                            ['var', 'y', 0], 
                                ['if', ['>', 'x', 10],
                                ['set', 'y', 20], 
                                ['set', 'y', 30],
                                ],
                                'y']), 30, "If block Failed")



        # while loop
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'c', 0],
                            ['var', 'r', 0], 
                                ['while', ['<', 'c', 10],
                                ['begin', 
                                ['set', 'r', ['+', 'r', 1]], 
                                ['set', 'c', ['+', 'c', 1]],
                                ]],
                                'r']), 10, "While Loop failed")


        # Factorial
        self.test(self.Interpreter.eval(['begin', 
                            ['var', 'fact', 9],
                            ['var', 'result', 1], 
                                ['while', ['>=', 'fact', 1],
                                ['begin', 
                                ['set', 'result', ['*', 'result', 'fact']], 
                                ['set', 'fact', ['-', 'fact', 1]],
                                ]],
                                'result']), 362880, "Factorial failed")
        

        # Print Function (Global)
        self.test(self.Interpreter.eval(["print", "x", 90]), None, "Print Function Error")
        self.test(self.Interpreter.eval(["print", "\"Hi, This is an Interpreter\""]), None, "Print Function Error")


        # User-Defined Functions
        self.test(self.Interpreter.eval(['begin', 
                                            ['def', 'square', ["x"], ["*", "x", "x"]],
                                            ["square", 2]]), 4, "Factorial failed")
        
        self.test(self.Interpreter.eval(['begin', 
                                            ['def', 'mul', ["x", "y"], ["*", "y", "x"]],
                                            ["mul", 2, 9]]), 18, "Factorial failed")

        print("\nCompleted Tests:", auto_test.ctest + auto_test.dtest)
        print("Success:", auto_test.ctest)        
        print("Failed:", auto_test.dtest)        

