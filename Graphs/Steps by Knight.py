"""
We have to find the minimum steps the knight has to take to reach the target positon
approach:
>> use bfs and count the number of levels we have to go thro before reaching the target
"""
class Solution:

	#Function to find out minimum steps Knight needs to reach target position.
	def minStepToReachTarget(self, KnightPos, TargetPos, N):
		
		queue = [KnightPos]
		count = 0
		
		moves = [(-2,-1),(-2,1),(2,-1),(2,1),(-1,-2),(1,-2),(-1,2),(1,2)]
		
		visited = []
		for x in range(N+1):
		    list1 = []
		    for y in range(N+1):
		        list1.append(False)
            visited.append(list1)
		
		visited[TargetPos[0]][TargetPos[1]] = True
		
		while len(queue) > 0:
		    
		    count += 1
		    size = len(queue)
		    
		    for _ in range(size):
		        
		        curr = queue.pop(0)
		        i = curr[0]
		        j = curr[1]
		        
		        for move in moves:
		            curri = i + move[0]
		            currj = j + move[1]
		            
		            if curri <= N and currj <= N and curri >0 and currj > 0:
		                if TargetPos[0] == curri and TargetPos[1] == currj:
		                    return count 
		                else:
		                    queue.append((curri,currj))
                            visited[curri][currj] = True
                            
        return 0