def printLL(head):
    while head != None:
        print(head.data,end="->")
        head = head.next
    print("None")

class LinkedList:
    def __init__(self):
        self.head = None 

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def removeDup(head):

    dict1 = {}
    curr = head
    prevUnique = head
    
    while curr != None:

        if curr.data in dict1:
            # this is a duplicate and we need to remove it 
            prevUnique.next = curr.next
            curr = curr.next

        else:
            dict1[curr.data] = 1
            prevUnique = curr
            curr = curr.next

    return head

ll = LinkedList()
ll.head = Node(2)
ll.head.next = Node(4)
ll.head.next.next = Node(5)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(6)
ll.head.next.next.next.next.next = Node(7)
ll.head.next.next.next.next.next.next = Node(4)

printLL(ll.head)
newHead = removeDup(ll.head)
printLL(newHead)



