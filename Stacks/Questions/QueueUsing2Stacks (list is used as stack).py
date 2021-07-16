'''
Stack reverses the order of element
In a Queue the order remains the same
List is used as stack in this
'''
class QueueUsing2Stack():

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self,item):
        self.instack.append(item)

    def dequeue(self):
        if self.instack != []:
            while self.instack != []:
                element = self.instack.pop()
                self.outstack.append(element)
        return self.outstack.pop()

q = QueueUsing2Stack()

for i in range(5):
    q.enqueue(i)
    
for i in range(5):
    print(q.dequeue())