##### fibonacci is sum of last two nos

def fibonacci(n):
	# base condition
	if n ==1 or n ==2:
		return 1

	else:
		# big number goes on breaking until they hit the base condition and then start forming results until starting number is 
		# is reached
		return fibonacci(n-1) + fibonacci(n-2)


print(fibonacci(12))