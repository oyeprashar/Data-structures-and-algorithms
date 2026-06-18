
def isValidIndices(rowIndex, colIndex, matRows, matCols):

    if rowIndex >= 0 and rowIndex < matRows and colIndex >= 0 and colIndex < matCols:
        return True
    return False

def shortest_path(grid, sr, sc):

    # all four directions are allowed
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    queue = [(sr, sc)]
    grid[sr][sc] = [0, 0]
    dist = 0

    visited = []
    for i in range(len(grid)):
        currRow = []
        for j in range(len(grid[0])):
            currRow.append(False)
        visited.append(currRow)

    pathFound = False
    destRow = None
    destCol = None

    while queue:

        dist += 1

        for _ in range(len(queue)):


            curr = queue.pop(0)

            for dir in directions:

                newRow = curr[0] + dir[0]
                newCol = curr[1] + dir[1]
                # print(newRow, newCol)

                if isValidIndices(newRow, newCol, len(grid), len(grid[0])):

                    if grid[newRow][newCol] == 'E':
                        visited[newRow][newCol] = [curr[0], curr[1]]
                        pathFound = True
                        destRow = newRow
                        destCol = newCol
                        break

                    if visited[newRow][newCol] == False and grid[newRow][newCol] != '#':
                        queue.append((newRow, newCol))
                        visited[newRow][newCol] = [curr[0], curr[1]]

            if pathFound:
                break


    if not pathFound:
        return -1

    path = []
    while not (destRow == 0 and destCol == 0): # While we are not at the source node
 
        path.append([(destRow, destCol)])
        curr = visited[destRow][destCol]
        destRow = curr[0]
        destCol = curr[1]

    path.append([0,0])
    return path[::-1]


grid = [['S','.','.','#','.','.','.'],
        ['.','#','.','.','.','#','.'],
        ['.','#','.','.','.','.','.'],
        ['.','.','#','#','.' ,'.', '.'],
        ['#','.','#','E','.','#','.']]


print(shortest_path(grid, 0, 0))

