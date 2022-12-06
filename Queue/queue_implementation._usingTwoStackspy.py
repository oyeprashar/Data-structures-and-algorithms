'''
Stack reverses the order of element
In a Queue the order remains the same
Stack class is implemented
'''
class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class QueueUsing2Stack(Stack):

    def __init__(self):
        self.instack = Stack()
        self.outstack = Stack()

    def enqueue(self,item1):
        self.instack.push(item1)

    def dequeue(self):
        if self.instack.isEmpty() != True:
            while self.instack.isEmpty() != True:
                element = self.instack.pop()
                self.outstack.push(element)
        if self.outstack.isEmpty() != True:
            return self.outstack.pop()

q = QueueUsing2Stack()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())