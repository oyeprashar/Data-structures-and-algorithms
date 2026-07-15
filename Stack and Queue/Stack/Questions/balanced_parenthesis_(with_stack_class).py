class Stack():
	def __init__(self):
		self.items = []
	def push(self,item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def peek(self):
		return self.items[len(self.items)-1]
	def isEmpty(self):
		return self.items == []
	def size(self):
		return len(self.items)

def is_parenthesis_balanced(s):
	opening = set('([{')
	matches = set([ ("(",")"), ("[","]"), ("{","}")])
	balanced = True
	stack = Stack()

	if len(s)%2 != 0:
		balanced = False

	else:
		for paren in s:
			if paren in opening:
				stack.push(paren)

			else:
				if stack.size() == 0:
					balanced = False
				else:	
					last_open = stack.pop()

					if (last_open,paren) not in matches:
						balanced = False

	return stack.size() == 0 and balanced == True


print(is_parenthesis_balanced('{{[[(())]]}}'))
	

