"""
Rotate doubly linkedlist by N nodes
Input : a  b  c  d  e   N = 2
Output : c  d  e  a  b 

Input : a  b  c  d  e  f  g  h   N = 4
Output : e  f  g  h  a  b  c  d 
"""

def printLL(head):
    while head.next != None:
        print(head.data,end="->")
        head = head.next
    print(head.data)

    while head.prev != None:
        print(head.data,end="->")
        head = head.prev
    print(head.data)

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def rotate(head,n):

    count = 0

    start = head
    end = None

    curr = head

    while curr != None and count != n:
        count += 1
        end = curr
        curr = curr.next

    head = curr
    head.prev = None
    end.next = None

    last = head
    while last.next != None:
        last = last.next

    last.next = start 
    start.prev = last

    return head


node1 = Node("a")
node2 = Node("b")
node3 = Node("c")
node4 = Node("d")
node5 = Node("e")
node6 = Node("f")
node7 = Node("g")
node8 = Node("h")

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

node2.prev = node1
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
node7.prev = node6
node8.prev = node7


printLL(node1)
node1 = rotate(node1,4)
print()
printLL(node1)