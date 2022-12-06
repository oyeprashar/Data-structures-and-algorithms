"""
Design a data structure that supports insert, delete, search and getRandom in constant time
"""
import random 

class CustomDS:

    def __init__(self):
        self.dictionary = {}


    def push(self,data):
        
        if data in self.dictionary:
            self.dictionary[data] += 1
        
        else:
            self.dictionary[data] = 1
        
    def pop(self,data):

        if self.dictionary[data] > 1:
            self.dictionary[data] -= 1
        
        else:
            self.dictionary.pop(data)
        
    def search(self,data):

        if data in self.dictionary:
            return True 
        else:
            return False 
        
    def getRandom(self):
        return random.choice(list(self.dictionary.keys()))

ds = CustomDS()
ds.push(10)
ds.push(20)
ds.push(30)
ds.push(40)
print(ds.search(30))
ds.pop(20)
ds.push(50)
print(ds.search(50))
print(ds.getRandom())







    