import heapq

class Node:
    def __init__(self,char,count):
        self.char = char
        self.count = count
        self.huff = None

        self.left = None
        self.right = None

    def __lt__(self,otherObject):
        return self.count < otherObject.count

def encode(root,key,ans):
    if root.char == key:
        return

    elif key in root.left.char:
        ans.append(root.left.huff)
        encode(root.left,key,ans)

    elif key in root.right.char:
        ans.append(root.right.huff)
        encode(root.right,key,ans)


def preorder(root,keyList,orderedList):
    if root:
        if root.char in keyList:
            orderedList.append(root.char)
        preorder(root.left,keyList,orderedList)
        preorder(root.right,keyList,orderedList)

def buildTree(list1):
    objectList = []

    for i in range(len(list1)):
        char = list1[i][0]
        count = list1[i][1]
        currObj = Node(char,count)
        objectList.append(currObj)

    heapq.heapify(objectList)
    # print(len(objectList))
    root = 0

    while len(objectList) != 1:
        # print("-------")
        smallest1 = heapq.heappop(objectList)
        # print("smallest1 =",smallest1.char," its count =",smallest1.count)
        smallest2 = heapq.heappop(objectList)
        # print("smallest2 =", smallest2.char, " its count =", smallest2.count)

        newChar = smallest1.char + smallest2.char
        newCount = smallest1.count + smallest2.count

        newNode = Node(newChar,newCount)
        root = newNode
        newNode.left = smallest1
        newNode.left.huff = 0
        newNode.right = smallest2
        newNode.right.huff = 1

        heapq.heappush(objectList,newNode)

        # print("NewNode char=",newNode.char," newNode count =",newNode.count," its right =",newNode.right.char," its rights huff = ",newNode.right.huff," its left =",newNode.left.char," its lefts huff =",newNode.left.huff)

    return objectList[0]


def huffmanCodes(S,f,N):
    list1 = []
    for i in range(len(f)):
        list1.append((S[i],f[i]))

    root = buildTree(list1)
    orderedList = []
    keys = [char for char in S]
    preorder(root,keys,orderedList)
    res = []
    for key in orderedList:
        currAns = []
        encode(root,key,currAns)
        currAns = [str(num) for num in currAns]
        str1 = "".join(currAns)
        res.append(str1)

    return res

S = "abcdef"
f = [5, 9, 12, 13, 16, 45]
print(huffmanCodes(S,f,12))










