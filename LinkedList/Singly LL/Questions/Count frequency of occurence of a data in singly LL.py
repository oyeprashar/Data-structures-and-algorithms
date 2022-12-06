class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList():
    def __init__(self):
        self.head = None
    def printList(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            temp1 = self.head
            while(temp1):
                print(temp1.data)
                temp1 = temp1.next
    def getrecursiveOccurence(self,node1,key,counter):
        # NOTE: Base case/terminating condition
        if node1 is None:
            return counter # When LL ends the function is terminated

        if node1.data == key:
            counter = counter + 1
        
        return self.getrecursiveOccurence(node1.next,key,counter)
    def recursiveOccurence(self,key):
        counter = 0 
        node1 = self.head
        return self.getrecursiveOccurence(node1,key,counter)
    
    def iterativeOccurence(self,key):
        if self.head is None:
            return "LinkedList is empty"
        else:
            temp2 = self.head
            count = 0
            while(temp2):
                if temp2.data == key:
                    count = count + 1
                temp2 = temp2.next
            return count


llist = LinkedList()
llist.head = Node(11)
second = Node(22)
third = Node(33)
fourth = Node(44)
fifth = Node(66)
sixth = Node(66)

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = sixth

print(llist.recursiveOccurence(66))
print() # prints a blank line

print(llist.iterativeOccurence(44))