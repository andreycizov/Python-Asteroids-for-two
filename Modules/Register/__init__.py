'''
Register class for objects for the Physics interaction
03.12.2010 Andrej Cizov
'''

class Register():
        def __init__(self):
                self.list = []
                
        def add(self, obj):
                self.list.append(obj)
                
        def flush(self):
                self.list = []
                
        def remove(self, obj):
                try:
                        self.list.remove(obj)
                except ValueError:
                        pass
                
        def items(self):
                return self.list
                
        def __getitem__(self, i):
                return self.list[i]
