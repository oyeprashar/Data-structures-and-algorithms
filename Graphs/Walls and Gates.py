"""
LeetCode 286. Walls and Gates

    You are given an m x n 2D grid rooms initialized with these three possible values:

        * -1 → A wall or an obstacle.
        * 0 → A gate.
        * 2147483647 → An empty room.

    Your task is to fill each empty room with the distance to its nearest gate

Example :
        Input :
            [
              [INF, -1,  0, INF],
              [INF, INF, INF, -1],
              [INF, -1, INF, -1],
              [ 0, -1, INF, INF]
            ]

        Output :
            [
              [3, -1, 0, 1],
              [2, 2, 1, -1],
              [1, -1, 2, -1],
              [0, -1, 3, 4]
            ]


Approach :
    The approach is pretty simple! Instead of counting the steps from each empty cell to the nearest gate we do the
    opposite, count the number of steps from gate to each empty cell. This means, we can append all the gates to the
    queue and run one BFS to get the answer instead of running BFS multiple times from each empty cell

    TC : O(n*m)

"""

from collections import deque


class Solution:

    def wallsAndGates(self, rooms):

        """
        0          : gate
        -1         : wall
        2147483647 : Empty call
        """

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dq = deque()
        empty = 2147483647

        # append all the gates to the queue
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    dq.append([i, j])

        while dq:

            curr = dq.popleft()

            for dr, dc in directions:
                newRow = curr[0] + dr
                newCol = curr[1] + dc
                if newRow >= 0 and newRow < len(rooms) and newCol >= 0 and newCol < len(rooms[0]):
                    if rooms[newRow][newCol] == empty:
                        dq.append([newRow, newCol])
                        rooms[newRow][newCol] = 1 + rooms[curr[0]][curr[1]]

        return rooms


INF = 2147483647
rooms = [
    [INF, -1, 0, INF],
    [INF, INF, INF, -1],
    [INF, -1, INF, -1],
    [0, -1, INF, INF]
]

s = Solution()
print(s.wallsAndGates(rooms))
