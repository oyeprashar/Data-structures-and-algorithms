class Stack():
	# listing the attributes
	def __init__(self):
		self.items = []

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return len(self.items) == 0 

	def push(self,item):
		self.items.append(item)

	def pop(self):
		if not self.isEmpty():
			return self.items.pop()
		else:
			return "UNDERFLOW"
			
	def peek(self):
		return self.items[(len(self.items))-1]


s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())
print(s.isEmpty())
print(s.pop())

