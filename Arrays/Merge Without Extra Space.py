
# better and efficient approach | max(nlogn.mlogm)
class Solution:
    
    #Function to merge the arrays.
    def merge(self,arr1,arr2,n,m):
    
        i = len(arr1)-1
        j = 0
            
            
        while i >= 0 and j < len(arr2) and arr1[i] > arr2[j]:
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i -= 1
            j += 1
        
        arr1.sort()
        arr2.sort()
        
        return arr1,arr2




# using insertion sort algo but this takes O(m*n)
def merge(arr1,arr2):


    j = len(arr2) - 1 

    while j >= 0:

        i = len(arr1) - 2
        swapHua = False
        last = arr1[-1]

        while i >= 0 and arr1[i] > arr2[j]:
            arr1[i+1] = arr1[i]
            swapHua = True
            i -= 1

        # even if the loop doesn't work and and arr1 ke last prr jo element betha hai that is greator than element at jth index of arr2, we swap them
        # because we want all bigger element to be in arr2 and smaller in arr1
        if swapHua == True or last > arr2[j]:
            arr1[i+1] = arr2[j]
            arr2[j] = last

        j -= 1
    return arr1,arr2


arr1 = [10]
arr2 = [2, 3]
# arr1 = [1, 5, 9, 10, 15, 20]
# arr2 = [2, 3, 8, 13]
print(merge(arr1,arr2))