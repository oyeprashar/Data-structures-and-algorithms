class Node:

	def __init__(self,data):
		self.data = data
		self.next = None 


def printLL(head):
    while head.next != None:
        print(head.data,end="->")
        head = head.next
    print(head.data)


def findSize(head):
	count = 0 
	curr = head 
	last = None 

	while curr != None:
		count += 1
		last = curr
		curr = curr.next 

	return count,last

def segregate(head):

	size,last = findSize(head)
	count = 0
	curr = head 
	prev = None
	newHead = None 

	while count != size:
		nextNode = curr.next 

		if curr.data % 2 == 1:
			if prev == None:
				newHead = curr.next 
				curr.next = None 

			else:
				prev.next = curr.next 
				curr.next = None 

			last.next = curr 
			last = last.next 

		curr = nextNode 
		count += 1

	return newHead


n1 = Node(17)
n2 = Node(15)
n3 = Node(8)
n4 = Node(9)
n5 = Node(2)
n6 = Node(4)
n7 = Node(6)

n1.next = n2 
n2.next = n3 
n3.next = n4 
n4.next = n5 
n5.next = n6 
n6.next = n7

printLL(n1)
newHead = segregate(n1)
printLL(newHead)











