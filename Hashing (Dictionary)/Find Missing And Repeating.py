"""
Suppose there is an array from 1 to N, given a subset we need to find the missing number and the repeating number

==== LOGIC ===
-> generate a dictionary with all elements of the array
-> now start traversing from range 1 till N 
    -> if the element is not in the dictinary, append it to the missing array
    -> if the element is having frequency more than once then append it to repeating array
-> return repeating.extended(missing)
"""

class Solution:
    def findTwoElement( self,arr, n):
        dict1 = {}
        for num in arr:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1
        # output = repeating number, missing number
        repeated = []
        missing = []
        for num in range(1,n+1):
            
            if num in dict1 and dict1[num] > 1:
                repeated.append(num)
            
            elif num not in dict1:
                missing.append(num)
        repeated.extend(missing)
        return repeated