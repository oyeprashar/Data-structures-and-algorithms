"""
Input:
N = 3, W = 50
values[] = {60,100,120}
weight[] = {10,20,30}
Output:
240.00
Explanation:Total maximum value of item
we can have is 240.00 from the given
capacity of sack. 
"""

def fractionalKnapsack(value,weight,W):
	# W is the capacity of our sack

	item = []
	for i in range(len(value)):
		valuePerWeight = value[i] / weight[i] 
		item.append((valuePerWeight,value[i],weight[i]))

	item.sort(reverse=True)
	bag = 0
	totalCollected = 0
	for i in range(len(item)):
		# print("current bag =",bag,"totalCollected =",totalCollected)
		if bag == W:
			break

		if bag + item[i][2] <= W:
			bag += item[i][2]
			totalCollected += item[i][1]

		else:
			canTake = W-bag
			bag += canTake
			totalCollected += canTake * item[i][0]
	
	return totalCollected



# value = [60,100,120]
# weight = [10,20,30]
# W = 50	

W = 50
value = [60,100]
weight = [10,20]
print(fractionalKnapsack(value,weight,W))