#01 knapsack problem
# inputs are W --> capacity of kanpsack
#			 n --> no of items
#			 wt --> list of weights of the items
#			 v --> list of values of the items

def knapsack(W,n,wt,v):
	# if capacity is zero or no item is left return 0
	# base case where program terminates 
	if W==0 or n ==0: 
		return 0

	# we are starting for the back i.e. n-1
	# if the weight of a specific element is greator then capacity we'd LEAVE that element and MOVE
	if wt[n-1] > W:
		return knapsack(W,n-1, wt, v)
	else:
		# Why are we returning the max of Selecting or not selecting an element?
		# Because we are trying to find the max value if we select that element or we skip that element dispite the fact that its
		# weight is equal or under our knapsack capacity (W)
		# max of two cases:
		# i)  selecting the element
		# ii) 
		return max(v[n-1] + knapsack(W-wt[n-1], n-1, wt, v), knapsack(W, n-1, wt, v))


wt = [10, 20, 30]
v = [60, 100, 120]
W = 50
n = len(v)
print(knapsack(W,n,wt,v))