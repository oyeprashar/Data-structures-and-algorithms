"""
1
15 8 3
3 8
11 2
8 6
"""
test_cases = int(input())
for _ in range(test_cases):
    xRange,yRange,numofTowers = map(int,input().split())
    xCoordinates = []
    yCoordinates = []

    for i in range(numofTowers):
        x,y = map(int,input().split())
        xCoordinates.append(x)
        yCoordinates.append(y)

    xCoordinates = sorted(xCoordinates)

    deltaX = []
    for j in range(1,len(xCoordinates)):
        curr = xCoordinates[j] - xCoordinates[j-1] - 1
        # print("xCoordinates[j] =",xCoordinates[j]," xCoordinate[j-1] =",xCoordinates[j-1]," their diff =",curr)
        deltaX.append(curr)

    firstX = xCoordinates[0] - 0 - 1
    deltaX.append(firstX)

    lastX = (xRange + 1) - xCoordinates[-1] - 1
    deltaX.append(lastX)

    yCoordinates = sorted((yCoordinates))
    deltaY = []
    for k in range(1, len(yCoordinates)):
        curr = yCoordinates[k] - yCoordinates[k - 1] - 1
        # print("xCoordinates[j] =",xCoordinates[j]," xCoordinate[j-1] =",xCoordinates[j-1]," their diff =",curr)
        deltaY.append(curr)

    firstY = yCoordinates[0] - 0 - 1
    deltaY.append(firstY)

    lastY = (yRange + 1) - yCoordinates[-1] - 1
    deltaY.append(lastY)

    print( max(deltaX) * max(deltaY))
