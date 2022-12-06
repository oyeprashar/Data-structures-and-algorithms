"""
Implementation of doubly linked list
"""

class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def check(head):
    curr = head 

    while curr.next != None:
        print(curr.data,end="->")
        curr = curr.next
    print(curr.data)

    while curr.prev != None:
        print(curr.data,end="->")
        curr = curr.prev
    print(curr.data)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)

ll = LinkedList()
ll.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4

check(ll.head)