"""
1) push() which adds an element to the top of stack. 
2) pop() which removes an element from top of stack. 
3) findMiddle() which will return middle element of the stack. 
4) deleteMiddle() which will delete the middle element. 
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
        self.prev = None 
    
class Stack:
    def __init__(self):
        self.top = Node(None)
        self.length = 0
        self.mid = None
    
    def push(self,data):
        newNode = Node(data)

        if self.length == 0:
            self.top = newNode 
            self.mid = self.top 
            self.length += 1
        
        else:

            self.top.next = newNode
            newNode.prev = self.top 
            self.top = newNode 
            
            if self.length % 2 == 1:
                self.mid = self.mid.next 
            
            self.length += 1
        
    def pop(self):
        
        if self.top.data == None:
            return "EMPTY"
        
        if self.top.prev == None:
            removed = self.top.data 
            self.top.data = None
            return removed

        removed = self.top.data
        self.top = self.top.prev 
        
        self.top.next = None 

        if self.length % 2 == 0:
            self.mid = self.mid.prev 
        

        self.length -= 1
        
        return removed 
    
    def getMid(self):

        if self.top == None:
            return "EMPTY"
        
        return self.mid.data 
    
    def deleteMid(self):
        if self.top == None:
            return "EMPTY"

        if self.length == 1:
            self.mid = self.top 
            self.top.data = None
        
        curr = self.mid 

        if self.length % 2 == 0:
            self.mid = self.mid.prev 
        
        else:
            self.mid = self.mid.next 
        
        curr.prev.next = curr.next 
        curr.next.prev = curr.prev

s = Stack()
s.push(5)
# print(s.top.data,s.getMid())
s.push(6)
# print(s.top.data,s.getMid())
s.push(7)
# print(s.top.data,s.getMid())
s.push(8)
# print(s.top.data,s.getMid())
s.push(9)
# print(s.top.data,s.getMid())

print("---------------------------------")
print(s.pop(),s.getMid())
print("---------------------------------")
print(s.pop(),s.getMid())
print("---------------------------------")
print(s.pop(),s.getMid())
print("---------------------------------")
print(s.pop(),s.getMid())
print("---------------------------------")
print(s.pop(),s.getMid())
print("---------------------------------")
