# Environment Class
# Repository for variables and functions defined in the program

class env:
    def __init__(self, parent=None) -> None:
        self.record = {'True': True, 'False': False, 'None': None}
        self.parent = parent


    def define(self, name, value):
        self.record[name] = value
        return True


    def assign(self, name, value):
        self.resolve(name).record[name] = value
        return True

    
    def lookup(self, name):
        return self.resolve(name).record.get(name)


    def resolve(self, name):

        if (self.record.get(name) != None):
            return self
        
        if (self.parent == None):
            raise NameError
        
        return self.parent.resolve(name)