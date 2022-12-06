# IMPORTANT
# Rules:
#  1) if row == 0 or cloumn == 0 K[row][col] = 0
#  2) if weight of an element at row,col <= allowed weight in cell put value into it using K[i][w] = max(v[i-1] + K[i-1][w-wt[i-1]],K[i-1][w])
#  3) if weight is more than allowed weight then copy the elements from the prevous row

def knapsack_dynamic(W,n,wt,v):

	# Making a 2d list with rows   equal to weight(W) from 0 to W(capacity)
	# and columns equal to number of elements from 0 to n 
	#    0 --------→ W
	# 0  0 0 0 0 0 0 0
	# |  0 0 0 0 0 0 0     # For understanding the table (2d list) not same 
	# |  0 0 0 0 0 0 0
	# ↓  0 0 0 0 0 0 0
	# N  0 0 0 0 0 0 0
	
	# ALL THE ELEMENTS ARE ASSIGNED WITH ZERO
	
  	K = [[0 for x in range(W + 1)] for x in range(n + 1)]  # W + 1 and n + 1 are used since range does not include the last element
  	# now assigning values to each cell
  	for i in range(n + 1): # i is from 0--------n (in range last element is not included)
  		for w in range(W + 1): # w is from 0--------W (in range last element is not included)
  			
  			if i == 0 or w == 0: # 0th row and 0th columns elements are ALWAYS ZERO
  				K[i][w] = 0
  			
  			elif wt[i-1] <= w:  # i-1 is used to check the weight of that element from back against allowed weight in that cell
  				K[i][w] = max(v[i-1] + K[i-1][w-wt[i-1]], K[i-1][w]) # max of if the element included or excluded 
  			
  			else:
  				K[i][w] = K[i-1][w] # if the weight is more that allowed weight in that cell then copy the value from previous row
  	
  	return K[n][W]


v = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(v)
print(knapsack_dynamic(W,n,wt,v)) 

