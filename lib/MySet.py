class MySet:
    def __init__(self, enumerable = []):
        self.dictionary = {}
        for value in enumerable:
            self.dictionary[value] = True
            
    def __str__(self):
        keys = {x for x in self.dictionary.keys()}
        keys_str = ','.join(str(x) for x in keys)
        return f"MySet: {{{keys_str}}}"
            
    def has(self, value):
        return value in self.dictionary
    
    def add(self, value):
        self.dictionary[value] = True
        return self
    
    def delete(self, value):
        self.dictionary.pop(value,None)
        return self
    
    def size(self):
        return len(self.dictionary)
    
    def clear(self):
        self.dictionary = {}
        return self
    
    

    
    
