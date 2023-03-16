# EVA Interpreter

class Eva_Interpreter():

    def __init__(self) -> None:
        pass


    def eval(self, exp, ent=0):
        # Self Evaluating Expression (int)
        if (type(exp) == int):
            return exp
        

        # Self Evaluating Expression (str)
        if (type(exp) == str and exp[0]=="\"" and exp[-1]=="\""):
            return exp[1:-1]
        

        # Operator Expressions
        if (exp[0] == "+"):  return self.eval(exp[1], ent) + self.eval(exp[2], ent)
        if (exp[0] == "-"):  return self.eval(exp[1], ent) - self.eval(exp[2], ent)
        if (exp[0] == "*"):  return self.eval(exp[1], ent) * self.eval(exp[2], ent)
        if (exp[0] == "/"):  return self.eval(exp[1], ent) / self.eval(exp[2], ent)
        if (exp[0] == "//"): return self.eval(exp[1], ent) // self.eval(exp[2], ent)
        if (exp[0] == "**"): return self.eval(exp[1], ent) ** self.eval(exp[2], ent)

        if (exp[0] == ">"):  return self.eval(exp[1], ent) > self.eval(exp[2], ent)
        if (exp[0] == "<"):  return self.eval(exp[1], ent) < self.eval(exp[2], ent)
        if (exp[0] == ">="):  return self.eval(exp[1], ent) >= self.eval(exp[2], ent)
        if (exp[0] == "<="):  return self.eval(exp[1], ent) <= self.eval(exp[2], ent)        
        if (exp[0] == "=="):  return self.eval(exp[1], ent) == self.eval(exp[2], ent)

        if (exp[0] == "and"):  return self.eval(exp[1], ent) and self.eval(exp[2], ent)
        if (exp[0] == "or"):  return self.eval(exp[1], ent) or self.eval(exp[2], ent)
        if (exp[0] == "not"):  return not self.eval(exp[1], ent)
        

        raise ValueError("Unimplemented")