"""
first loop to check if we can use another vertex to go to dest in lesser cost
second loop to select a source
third loop to select a destination
"""
global INF
INF = 3 ** 38


def floydWarshall(graphMat, numberofVertices):
    distMat = graphMat
    for k in range(numberofVertices):  # first loop to check if we can go from src to destination in a lesser dst
        for i in range(numberofVertices):  # second loop to select src
            for j in range(numberofVertices):  # third loop to select dest
                # updating the smallest distance in our matrices (happens in place / realtime)
                distMat[i][j] = min(distMat[i][j], distMat[i][k] + distMat[k][j])
    return distMat


graph1 = [[0, 5, INF, 10],
          [INF, 0, 3, INF],
          [INF, INF, 0, 1],
          [INF, INF, INF, 0]
          ]
numberofVertices = 4
ans = floydWarshall(graph1, numberofVertices)
for listItem in ans:
    print(listItem)

