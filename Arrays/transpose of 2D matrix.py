dimension = int(input())
matrix = []
transpose = []
for row in range(dimension):
	entry = list(map(int,input().split())) # taking inputs like 1 2 3 and making list of these
	matrix.append(entry)

for i in range(dimension): 
	for j in range(dimension):
		transpose.append(matrix[j][i]) # in transpose j becomes i and i becomes j
		m = 0
n = dimension

for x in range(dimension+1):
	
	row = transpose[m:n] # making a list of items to be printed in a single line
	list1 = [str(item) for item in row]
	string2 = " ".join(list1) # converting the list into a string
	print(string2)
	# m and n are incremented so that only elements according to dimension is printed in one line
	m = n 
	n = n + dimension