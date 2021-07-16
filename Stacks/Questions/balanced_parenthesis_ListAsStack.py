def is_parenthesis_balanced(s):
	opening = set('([{')
	matches = set([ ("(",")"), ("[","]"), ("{","}")])
	balanced = True
	stack = [] 

	if len(s)%2 != 0:
		balanced = False

	else:
		for paren in s:
			if paren in opening:
				stack.append(paren)

			else:
				if len(stack) == 0:
					balanced = False

				last_open = stack.pop()

				if (last_open,paren) not in matches:
					balanced = False

	return len(stack) == 0 and balanced == True


print(is_parenthesis_balanced('()(){]}'))
	

