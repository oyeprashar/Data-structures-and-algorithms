"""
def insert(root,key):
    
    #code here

#Function to use TRIE data structure and search the given string.
def search(root, key):
    
    #code here
"""

class TrieNode:
    def __init__(self):
        self.charList = [None] * 26
        self.end = False


def insert(root,word):

    currNode = root

    for char in word:

        # if you already have a node for current character we move to it
        if currNode.charList[ord(char)-ord('a')] != None:
            currNode = currNode.charList[ord(char)-ord('a')]

        # else you will create that node and then move to it       
        else:
            newNode = TrieNode()
            currNode.charList[ord(char)-ord('a')] = newNode
            currNode = newNode

        currNode.end = True
    
def matchEntireWord(root,word):

    currNode = root
    for char in char:

        # if there is a node for current character we move to that character
        if currNode.charList[ord(char)-ord('a')] != None:
            currNode = currNode.charList[ord(char)-ord('a')]
        
        else:
            return False

        return currNode.end

def startsWith(root,word):

    currNode = root
    for char in char:

        # if there is a node for current character we move to that character
        if currNode.charList[ord(char)-ord('a')] != None:
            currNode = currNode.charList[ord(char)-ord('a')]
        
        else:
            return False

    return True


    



        
