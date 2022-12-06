class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head.next != None:
        print(head.data,end="->")
        head = head.next
    print(head.data)

def partition(low,high):
    
    prev = None
    i = low.next
    j = low.next
        
    while j != None and j != high.next:
    
        if j.data < low.data:
    
            temp = j.data
            j.data = i.data
            i.data = temp
            prev = i
            i = i.next
        
        j = j.next

    if prev == None:
        return low
            
    temp = low.data
    low.data = prev.data
    prev.data = temp
    
    return prev
        
def quickSortHelper(low,high):
    
    if low == None or high == None:
        return 
    
    if high == low:
        return 
    
    pi = partition(low,high)
    
    if pi != None:
        quickSortHelper(low,pi)
        
    if pi.next != None and pi.next.next != None:
        quickSortHelper(pi.next,high)
    
    return low
    


def quickSort(head):
    curr = head
    while curr.next != None:
        curr = curr.next
        
    low = head
    high = curr
    
    newHead = quickSortHelper(low,high)
    
    return newHead


node1 = Node(99)
node2 = Node(88)
node3 = Node(77)
node4 = Node(66)
node5 = Node(11)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

printLL(node1)

node1 = quickSort(node1)

printLL(node1)

