# ratio = value/weight
import operator
# we are importing operator so that we can sort the list by one element(ratio)
wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
n = len(wt)

# making list of [value, weight, value/weight]
list1 = []
for i in range(len(val)):
	list1.append ([val[i],wt[i],val[i]*1.0/wt[i]]) # multiplying with 1.0 so that we get value in float and not in int

list1 = sorted(list1,reverse=True,key=operator.itemgetter(2))


max_profit = 0
fractional_obj = 0

for i in range(n):
	# 0 --> value
	# 1 --> weight
	# 2 --> ratio 
	# if capacity is not zero and item weight is less than capacity
	if capacity >0 and list1[i][1] < capacity:
		capacity = capacity - list1[i][1]
		max_profit = max_profit + list1[i][0]

	elif capacity != 0 and list1[i][1] > capacity: # if we still have capacity left and current item exceeds our capacity then
		fractional_obj = i                         # then we have to take this item in fraction (this would be our last element)
		break # we are breaking the loop because if the weight of element is exceeding the capacity
			  # it implies that this must be the last element we can include 
if capacity > 0:
	max_profit = max_profit + capacity*list1[fractional_obj][2] 
							  # this gives value of item taken in fraction
	
	print(max_profit)
