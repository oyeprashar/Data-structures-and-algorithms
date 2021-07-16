"""
we need to find a valid maximum height
a valid height is where we can cut >= M metres 
"""

def isValid(currHeight,treeArray,target):
    cuttkiya = 0
    for tree in treeArray:
        if tree - currHeight > 0:
            cuttkiya += tree-currHeight

    return cuttkiya >= target


def findMaxHeight(left,right,treeArray,target,ans):

    if left <= right:

        mid = (left+right) // 2

        if isValid(mid,treeArray,target):
            ans[0] = mid
            return findMaxHeight(mid+1,right,treeArray,target,ans)
        else:
            return findMaxHeight(left,mid-1,treeArray,target,ans)

def find(treeArray,target):
    ans = [-1]
    right = max(treeArray)
    findMaxHeight(0,right,treeArray,target,ans)
    return ans[0]


treeArray = [4, 42, 40, 26, 46]; target = 20
print(find(treeArray,target))

