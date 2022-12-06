def shortestPath(sr,sc,grid):

    visited = []
    for x in range(len(grid)):
        list1 = []
        for y in range(len(grid[0])):
            list1.append(False)
        visited.append(list1)

  
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]

    desti = -1
    destj = -1

    queue = [(sr,sc)]
    visited[sr][sc] = (0,0)
    found = False

    while len(queue) > 0:
        # print(1)
        curr = queue.pop(0)
        currR = curr[0]
        currC = curr[1]


        for x in range(4):
            nbrR = currR + dr[x]
            nbrC = currC + dc[x]

            if nbrR >= 0 and nbrC >= 0 and nbrR < len(grid) and nbrC < len(grid[0]):

                if visited[nbrR][nbrC] == False and grid[nbrR][nbrC] != "#":

                    visited[nbrR][nbrC] = (currR,currC)
                    queue.append((nbrR,nbrC))

                    if grid[nbrR][nbrC] == "E":

                        desti = nbrR
                        destj = nbrC
                        found = True

        if found == True:
            break
    
    if desti == -1 and destj == -1:
        return -1

    path = []

    check = 15
    count = 0

    for list1 in visited:
        print(list1)

    while desti != 0 or destj != 0:

        count += 1
        path.append([desti,destj])
        curr = visited[desti][destj]
        desti = curr[0]
        destj = curr[1]

    path.append((sr,sc))

    return path[::-1]


grid = [['S','.','.','#','.','.','.'],
        ['.','#','.','.','.','#','.'],
        ['.','#','.','.','.','.','.'],
        ['.','.','#','#','.' ,'.', '.'],
        ['#','.','#','E','.','#','.']]

print(shortestPath(0,0,grid))

