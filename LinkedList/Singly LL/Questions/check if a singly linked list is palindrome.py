# NOTE: logic to check palidrom in singly LL is:
#           1) first traverse the LL and push data into stack
#           2) again traverse the LL and pop from stack and compare

class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        # checking if the stack is already empty
        if not(self.isEmpty()):
            return self.items.pop()
        else:
            return "Stack is already empty"
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def checkPalindrome(self):
        if self.head is None:
            print("The LinkedList is empty")
        else:
            stack1 = Stack()
            temp = self.head
            while(temp):
                stack1.push(temp.data)
                temp = temp.next
            temp1 = self.head

            while(temp1):
                item = stack1.pop()
                if temp1.data == item:
                    palidrome1 = True
                else:
                    palidrome1 = False
                    break
                temp1 = temp1.next
            return palidrome1                       

llist = LinkedList()
llist.head = Node(1)
second = Node(2)
third = Node(3)
fourth = Node(4)
five = Node(3) 
six = Node(2) 
seven = Node(1) 

llist.head.next = second
second.next = third
third.next = fourth
fourth.next = five
five.next = six
six.next = seven

print(llist.checkPalindrome())
