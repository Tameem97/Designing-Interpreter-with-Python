# Environment Class
# Repository for variables and functions defined in the program

class env:
    def __init__(self, parent=None, record=None) -> None:
        self.record = {'True': True, 'False': False, 'None': None, 'print': self.funct1}
        if (record != None): self.record = {**self.record, **record}
        self.parent = parent


    # Built-in Print Function
    def funct1(self, *args):
        print(*args)
        return None


    # Defines a variable
    def define(self, name, value):
        self.record[name] = value
        return value


    # Assign a Value to a variable 
    def assign(self, name, value):
        self.resolve(name).record[name] = value
        return value

    
    # Search variable 
    def lookup(self, name):
        return self.resolve(name).record.get(name)


    # Manages Scope Resolution for variables
    def resolve(self, name):
        if (self.record.get(name) != None):
            return self
        
        if (self.parent == None):
            raise NameError(f"The variable {name} is not defined or out of scope!")
        
        return self.parent.resolve(name) 