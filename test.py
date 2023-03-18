import ast
import os

class auto_test:

    ctest =0

    def __init__(self, Interpreter) -> None:
        self.Interpreter = Interpreter


    def tests(self):
        dir = os.listdir("./Tests")
        for i in dir:
            read_file = open("./Tests/"+i, "r")
            self.Interpreter.eval(ast.literal_eval(read_file.read().rstrip()))
            auto_test.ctest+=1;
            read_file.close()
        

        print("\nAll Tests Passed...\nTotal Tests:", auto_test.ctest)
      