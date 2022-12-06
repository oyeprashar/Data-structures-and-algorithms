"""
Given unsorted array of flight tickets(pair of source and destination place) . 
Output a list with cities in order they are visited. Eg [[A,B] ,[C,D], [B,C]]. 
So clearly the only possible travel patternwould be A->B->C->D.
Also there is "no" round trip.

"""
def getPath(arr):
    dict1 = {}

    for list1 in arr:
        dict1[list1[0]] = list1[1]

    # print(dict1)

    start = arr[0][0]
    ans = [start]
    key = start 

    while key in dict1:
        ans.append(dict1[key])
        key = dict1[key]

    return "->".join(ans)

arr = [["A","B"] ,["C","D"], ["B","C"]]
arr = [["A","D"],["D","B"],["B","C"]]
print(getPath(arr))