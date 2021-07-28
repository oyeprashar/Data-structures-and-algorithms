"""
grid =  [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]
"""

def uniquePathsWithObstacles(grid):

    if grid[0][0] == 1:
        return 0

    if len(grid) == 1 and len(grid[0]) == 1:
        return 1

    memory = []
    for x in range(len(grid)):
        list1 = []
        for y in range(len(grid[0])):
            list1.append(0)
        memory.append(list1)


    # filling the first row
    for j in range(1,len(grid[0])):
        if grid[0][j] == 1:
            break

        memory[0][j] = 1

    # filling the first column
    for i in range(1,len(grid)):
        if grid[i][0] == 1:
            break

        memory[i][0] = 1

    for x in range(1,len(grid)):
        for y in range(1,len(grid[0])):
            a = 0
            b = 0
            if grid[x][y] != 1:
                a = memory[x-1][y]
                b = memory[x][y-1]

            memory[x][y] = a + b

    return memory[len(memory)-1][len(memory[0])-1]

grid =  [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]




print(uniquePathsWithObstacles(grid))