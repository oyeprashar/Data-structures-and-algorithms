class Queue():
    # defining the attributes
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if not(self.isEmpty()):
            return self.items.pop()
        else:
            return "UNDERFLOW"
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.size())