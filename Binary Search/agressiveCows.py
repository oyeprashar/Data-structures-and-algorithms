def isValid(minDist,numCows,stalls):

    curr = stalls[0]
    placed = 1
    for i in range(1,len(stalls)):
        if stalls[i] - curr >= minDist:
            placed += 1
            curr = stalls[i]

    return placed >= numCows

def searchAns(left,right,numCows,stalls,ans):
    if left <= right:

        mid = (left+right) // 2

        if isValid(mid,numCows,stalls):
            # save it and maximize it by moving to the right
            ans[0] = mid
            return searchAns(mid+1,right,numCows,stalls,ans)
        else:
            # move to the left to find a valid ans
            return searchAns(left,mid-1,numCows,stalls,ans)

def findDist(numCows,stalls):
    ans = [-1]
    stalls.sort()
    minRange = 0; maxRange = stalls[-1]-stalls[0]
    searchAns(minRange,maxRange,numCows,stalls,ans)
    return ans[0]

test_cases = int(input())
for _ in range(test_cases):
    n,numCows = map(int,input().split())
    stalls = []
    for i in range(n):
        x = int(input())
        stalls.append(x)
    print(findDist(numCows,stalls))