

def findCount(i,j,n,keypad,moves,memory):

    if i < 0 or j < 0 or i >= len(keypad) or j >= len(keypad[0]):
        return 0
    
    if keypad[i][j] == -1:
        return 0 

    if n == 1:
        return 1 
    
    if n <= 0:
        return 0 
    
    num = keypad[i][j]

    if memory[num][n] != -1:
        return memory[num][n]
    
    count = 0

    count += findCount(i,j,n-1,keypad,moves,memory)

    for move in moves:
        count += findCount(i+move[0],j+move[1],n-1,keypad,moves,memory)
    
    memory[num][n] = count 
    return memory[num][n]

def getCount(n):

    keypad =   [[1,2,3],
		        [4,5,6],
		        [7,8,9],
		        [-1,0,-1]]  
            
    moves = [(-1,0),(1,0),(0,-1),(0,1)]

    totalCount = 0

    memory = []
    for x in range(10):
        list1 = []
        for y in range(n+1):
            list1.append(-1)
        memory.append(list1)


    for i in range(len(keypad)):
        for j in range(len(keypad[0])):

            if keypad[i][j] != -1:
                totalCount += findCount(i,j,n,keypad,moves,memory)
    
    return totalCount 

print(getCount(4))




