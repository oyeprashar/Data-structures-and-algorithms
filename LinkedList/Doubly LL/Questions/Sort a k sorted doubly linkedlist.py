"""
Sort a k sorted doubly linkedlist
3 <-> 6 <-> 2 <-> 12 <-> 56 <-> 8
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def printLL(head):
    while head.next != None:
        print(head.data,end="->")
        head = head.next    
    print(head.data)

def sortDLL(head,k):

    curr = head

    while curr != None:
        count = 0
        start = curr
        prevNode = curr

        while count != k and start.prev != None:
            count += 1
            start = start.prev

        count = 0
        while count != k and start != None:
            count != 1
            if start.data > prevNode.data:
                temp = start.data
                start.data = prevNode.data
                prevNode.data = temp
            start = start.next
        curr = curr.next

    return head
        


node1 = Node(3)
node2 = Node(6)
node3 = Node(2)
node4 = Node(12)
node5 = Node(56)
node6 = Node(8)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
printLL(node1)
node1 = sortDLL(node1,2)
printLL(node1)