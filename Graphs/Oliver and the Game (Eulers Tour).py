"""
9
1 2
1 3
2 6
2 7
6 9
7 8
3 4
3 5
1
1 9 1
"""
from collections import defaultdict

def DFS_timeStamping(currV,adj,visited,currTime,entry,exit):

	entry[currV] = currTime[0]
	currTime[0] += 1

	for nbr in adj[currV]:
		if nbr not in visited:
			DFS_timeStamping(nbr,adj,visited,currTime,entry,exit)

	exit[currV] = currTime[0]
	currTime[0] += 1


def check(a,b,entry,exit):
	if entry[b] > entry[a] and exit[a] > exit[b]:
		return True
	return False

adj = defaultdict(list)

n = int(input())
for _ in range(n-1):
	u,v = map(int,input().split())
	adj[u].append(v)


visited = set()
currTime = [1]
entry = [-1] * (n+1) 
exit = [-1] * (n+1) 

DFS_timeStamping(1,adj,visited,currTime,entry,exit)

# print(adj)
# print(entry)
# print(exit)


m = int(input())
for _ in range(m):
	qType,dest,src = map(int,input().split())

	if qType == 0:
		ans = check(dest,src,entry,exit)
	else:
		ans = check(src,dest,entry,exit)
	
	if ans == True:
		print("YES")
	else:
		print("NO")

	
	
