"""
Check if the given prorder is valid for BST
Input:  pre[] = {2, 4, 3}
Output: true

Input:  pre[] = {2, 4, 1}
Output: false

Input:  pre[] = {40, 30, 35, 80, 100}
Output: true
"""

def checkValidity(currIndex,max1,min1,arr):

    if currIndex[0] == len(arr):
        return 
    
    # incorrect postion hai toh return kr do
    if arr[currIndex[0]] <= min1 or arr[currIndex[0]] >= max1:
        return 
    
    currElement = arr[currIndex[0]]
    currIndex[0] += 1

    checkValidity(currIndex,currElement,min1,arr)
    checkValidity(currIndex,max1,currElement,arr)


def isValid(arr):
    max1 = 3**38
    min1 = -3**38

    currIndex = [0]

    checkValidity(currIndex,max1,min1,arr)

    return currIndex[0] == len(arr)

arr = [2, 4, 1]

print(isValid(arr))

    

