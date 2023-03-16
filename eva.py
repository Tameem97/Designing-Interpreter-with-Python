# EVA Interpreter

class Eva_Interpreter():

    def __init__(self) -> None:
        pass


    def eval(self, exp):
        # Self Evaluating Expression (int)
        if (type(exp) == int):
            return exp
        

        # Self Evaluating Expression (str)
        if (type(exp) == str and exp[0]=="\"" and exp[-1]=="\""):
            return exp[1:-1]
        

        raise ValueError("Unimplemented")