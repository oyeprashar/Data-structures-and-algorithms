class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None

    def printList(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp = self.head
            while(temp):
                print(temp.data)
                temp = temp.next

    def duplicate(self):
        dupl_dict = {}
        curr = self.head
        while(curr):
            if curr.data in dupl_dict:
                
                next_node = curr.next
                prev_node.next = next_node

            else:
                dupl_dict[curr.data] = 1
                prev_node = curr # prev_node is set to the last unique node which would be encounter when it is not in dictionary already(Hence else block is executed)

            curr = curr.next



llist = LinkedList()
llist.head = Node(11)
first = Node(22)
second = Node(33)
third = Node(33)
fourth = Node(22)
fifth = Node(11)

llist.head.next = first
first.prev = llist.head
first.next = second
second.prev = first
second.next = third
third.prev = second
third.next = fourth
fourth.prev = third
fourth.next = fifth
fifth.prev = fourth

print("====ORIGINAL LINKEDLIST====")
llist.printList()
print("====REMOVING DUPLICATES====")
llist.duplicate()
llist.printList()