"""
Input: ch = “geeksforgeeks”
Output: e
e is the first element that repeats

Input: str = “hello geeks”
Output: l
l is the first element that repeat
"""

def getIdx(str1):
    dict1 = {}
    for char in str1:
        dict1[char] = 0

    for char in str1:
        dict1[char] += 1
        if dict1[char] > 1:
        	return char

    

str1 = "geeksforgeeks"

print(getIdx(str1))
