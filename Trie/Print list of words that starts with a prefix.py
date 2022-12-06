"""
Design “Ls” command (search function) given a list of files in an array.
Hint: use tries.
Input: [“fun”, “funny”, “foo”, “spam”, “set”]
4
“Ls f”
“Ls fu”
“Ls s”
“Ls r”
Output: fun funny foo
fun funny
spam set
-1
"""

class TrieNode:

    def __init__(self):
        self.children = [None] * 26
        self.end = False



def insert(root,str1):

    currNode = root

    for char in str1:

        index = ord(char) - ord('a')

        if currNode.children[index] == None:
            currNode.children[index] = TrieNode()

        currNode = currNode.children[index]

    currNode.end = True

def matchWord(root,str1):

    currNode = root

    for char in str1:

        index = ord(char) - ord('a')

        if currNode.children[index] == None:
            return False

        currNode = currNode.children[index]

    return currNode.end


def startsWith(root,str1):

    currNode = root

    for char in str1:

        index = ord(char) - ord('a')

        if currNode.children[index] == None:
            return False

        currNode = currNode.children[index]

    return True

# Time complexity : O(l * l)
def DFS(currNode,currStr,res):

    if currNode.end == True:
        res.append("".join(currStr))

    for i in range(len(currNode.children)):

        if currNode.children[i] != None:

            char = chr(i + ord('a'))
            currStr.append(char)
            DFS(currNode.children[i],currStr,res)
            currStr.pop()

def getAllWordsWithPrefix(root,prefix):

    # step1: Find the node where last character of prefix points to

    currNode = root

    for char in prefix:
        index = ord(char) - ord('a')
        currNode = currNode.children[index]

    res = []
    currStr = []
    DFS(currNode,currStr,res)

    for i in range(len(res)):
        res[i] = prefix + res[i]

    return res


root = TrieNode()
insert(root,"fun")
insert(root,"funny")
insert(root,"foo")
insert(root,"spam")
insert(root,"set")

print(getAllWordsWithPrefix(root,"f"))