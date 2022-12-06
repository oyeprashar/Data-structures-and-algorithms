"""
Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}
"""

def convert(arr):

    arr.sort()

    i = 1
    j = 1

    # putting the j at the first postive element 
    for x in range(len(arr)):

        if arr[x] >= 0:
            j = x
            break 
    
    # convreting the array now 
    while i < len(arr):

        if arr[i] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j += 1
        
        i += 2
    
    
arr = [1, 2, 3, -4, -1, 4]
convert(arr)
print(arr)






