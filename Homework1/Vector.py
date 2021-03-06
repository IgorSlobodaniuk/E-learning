class Vector:
    """
    Link to task: https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4
    """
    def __init__(self, data):
        self.data = data
        
    @classmethod
    def create_istance(cls):
        return object.__new__(cls)
    
    def _validate_length(self, inst):
        if len(self.data) != len(inst.data):
            raise Exception
        
    def add(self, inst):
        self._validate_length(inst)
        new_inst = self.create_istance()
        new_inst.data = [x + y for x, y in zip(self.data, inst.data)]
        return new_inst
        
    def equals(self, inst):
        return self.data == inst.data
    
    def subtract(self, inst):
        new_inst = self.create_istance()
        new_inst.data = [x - y for x, y in zip(self.data, inst.data)]
        return new_inst
    
    def dot(self, inst):
        return sum([x * y for x, y in zip(self.data, inst.data)])
        
    def norm(self):
        return sum([x ** 2 for x in self.data]) ** 0.5
    
    def __str__(self):
        return f'{tuple(self.data)}'.replace(' ', '')
