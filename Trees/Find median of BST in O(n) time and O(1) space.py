class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

def countNodes(root,count):

    if root != None:

        countNodes(root.left,count)
        count[0] += 1
        countNodes(root.right,count)

def findMiddle2(root,currCount,targetCount,mids):

    if root != None:

        findMiddle2(root.left,currCount,targetCount,mids)

        currCount[0] += 1

        if currCount[0] == targetCount:
            mids[0] = root.data
        
        elif currCount[0] == targetCount + 1:
            mids[1] = root.data 

        findMiddle2(root.right,currCount,targetCount,mids)


def findMedian(root):

    totalCount = [0]

    countNodes(root,totalCount)

    totalCount = totalCount[0]

    targetCount = totalCount // 2

    mids = [None,None]
    currCount = [0]

    findMiddle2(root,currCount,targetCount,mids)

    if totalCount % 2 == 0:
        return (mids[0]+mids[1]) / 2
    
    else:
        return mids[1]

root = Node(20)
root.left = Node(8)
root.left.left = Node(4)
root.left.right = Node(12)
root.left.right.left = Node(10)
root.left.right.right = Node(14)
root.right = Node(22)

print(findMedian(root))



        







