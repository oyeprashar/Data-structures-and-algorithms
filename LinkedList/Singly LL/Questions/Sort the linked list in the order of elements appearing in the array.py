class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def printLL(head):
    while head.next != None:
        print(head.data,end="->")
        head = head.next
    print(head.data)


def sortLL(arr,head):

    # step 1 : create a hashmap with frequencies of element in LL
    dict1 = {}
    curr = head
    while curr != None:
        if curr.data not in dict1:
            dict1[curr.data] = 1 
        else:
            dict1[curr.data] += 1

        curr = curr.next

    curr = head
    index = 0
    while curr != None and index < len(arr):

        currElement = arr[index]
        freq = dict1[currElement]

        count = 0
        curr1 = curr

        curr = curr.next

        while curr1 != None and count != freq:
            
            count += 1
            curr1.data = currElement
            curr1 = curr1.next
            
        
        index += 1
        curr = curr1

    return head




node1 = Node(3)
node2 = Node(2)
node3 = Node(5)
node4 = Node(8)
node5 = Node(5)
node6 = Node(2)
node7 = Node(1)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

# printLL(node1)
# print("---------")
arr = [5,1,3,2,8]
node1 =sortLL(arr,node1)
printLL(node1)