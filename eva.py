from environment import env


# EVA Interpreter
class Eva_Interpreter():

    # Class Attribute
    global_env = env()


    def __init__(self) -> None:
        pass


    def eval(self, exp, ent=global_env):
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
        

        # Variable Declaration 
        if (exp[0] == "var"):
            _, name, value = exp
            return ent.define(name, self.eval(value, ent))


        # Variable Assignment 
        if (exp[0] == "set"):
            _, name, value = exp
            return ent.assign(name, self.eval(value, ent))
        

        # Block 
        if (exp[0] == 'begin'):
            blockenv = env(ent)
            result = None
            for i in exp[1:]:
                result = self.eval(i, blockenv)     
            return result


        # If Statement
        if (exp[0] == "if"):
            _, condition, consequent, alternate = exp
            return self.eval(consequent, ent) if (self.eval(condition, ent)) else self.eval(alternate, ent)


        # While Loop 
        if (exp[0] == "while"):
            result = None
            _, condition, body = exp
            while (self.eval(condition, ent)):
                result = self.eval(body, ent)

            return result


        # Functions - Built-in
        if (type(exp) == list):
            funct = self.eval(exp[0], ent);  
            args  = []
            if (str(type(funct)) == "<class 'method'>"):
                for i in exp[1:]:
                    args.append(self.eval(i, ent))

                return funct(*args)


        # Variable Lookup 
        if (ent.lookup(exp) != None):
            return ent.lookup(exp)


        raise ValueError(f"Unimplemented: {exp}")