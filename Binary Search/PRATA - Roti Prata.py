
def isValid(timeLimit,rankList,req):
    cooked = 0

    for rank in rankList:
        elapsedTime = 0
        r = 1

        while elapsedTime <= timeLimit:
            timeTaken = r * rank
            elapsedTime += timeTaken
            if elapsedTime <= timeLimit:
                cooked += 1
            r += 1
    return cooked >= req

def findingMinTime(left,right,rankList,req,ans):

    if left <= right:

        mid = (left+right) // 2

        if isValid(mid,rankList,req) == True:
            # save and move to left to minimize it
            ans[0] = mid
            return findingMinTime(left,mid-1,rankList,req,ans)
        else:
            return findingMinTime(mid+1,right,rankList,req,ans)

def findTime(rankList,req):
    right = 0
    c = 0
    slowestCook = rankList[0]
    r = 1
    while c <= req:
        right += slowestCook * r
        c += 1
        r += 1
    ans = [-1]
    findingMinTime(0,right,rankList,req,ans)
    return ans[0]



testCases = int(input())
for _ in range(testCases):
    req = int(input())
    arr = [int(num) for num in input().split()]
    rankList = arr[1:]
    print(findTime(rankList,req))






