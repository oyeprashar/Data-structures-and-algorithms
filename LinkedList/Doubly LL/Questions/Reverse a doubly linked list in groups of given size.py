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



def reverse(head,k):

    count = 0 
    curr = head
    prev = None

    while curr != None and count != k:
        count +=1

        nextNode = curr.next
        curr.next = prev
        curr.prev = nextNode
        prev = curr
        curr = nextNode

    if nextNode != None:
        prevNext = reverse(nextNode,k)
        head.next = prevNext
        prevNext.prev = head

    return prev


node1 = Node(10)
node2 = Node(8)
node3 = Node(4)
node4 = Node(2)
node5 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

node2.prev = node1
node3.prev = node2
node4.prev = node3
# node5.prev = node4
printLL(node1)
node1 = reverse(node1,2)
printLL(node1)







