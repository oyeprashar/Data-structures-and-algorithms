#### Reversing a string using recursion
## base conditon is when len of string is 1, function should return the string itself
def reverse_string(s):
	size = len(s)
	if len(s) == 1:
		return s
	else:
		print(s[size-1],end="")
		return reverse_string(s[0:size-1])
print(reverse_string("prashar"))