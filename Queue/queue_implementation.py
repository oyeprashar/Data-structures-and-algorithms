"""
Implement queue such that insertion and deletion both are O(1) operations
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # O(1)
    def insert(self, data):
        newNode = Node(data)
       
        if self.tail is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

     # O(1)
    def delete(self):

        if self.head is None:
            return

        temp = self.head
        self.head = self.head.next
        
        # no items for tail to point at
        if self.head is None:
            self.tail = None
        
        return temp.data

    def __str__ (self):

        ans = ""
        curr = self.head
        while curr:
            ans += str(curr.data)
            ans += " "
            curr = curr.next
        return ans

queue = Queue()
queue.insert(1)
queue.insert(2)
queue.insert(3)
queue.insert(4)
queue.delete()
queue.delete()
print(queue)

# print(queue)
# queue.delete()
# print(queue)


