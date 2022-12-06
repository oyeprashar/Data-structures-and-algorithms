class Solution:

    def printUnsorted(self,arr, n):
        
        minVal = 3**38
        maxVal = -3**38

        flag = False
        for i in range(1,len(arr)):

            # the unsorted part has started
            if arr[i] < arr[i-1]:
                flag = True

            if flag:
                minVal = min(minVal,arr[i])


        flag = False
        for j in range(len(arr)-2,-1,-1):

            # the unsorted part has started
            if arr[j] > arr[j+1]:
                flag = True

            if flag:
                maxVal = max(maxVal,arr[j])

        # now finding the start and end of the unsorted part
        
        # if there is an element greator than min of the unsorted part then this is the start
        for i in range(len(arr)):
            if arr[i] > minVal:
                break

        # traversing from the end and checking if we have an element there lesses than max of unsorted
        for j in range(len(arr)-1,-1,-1):
            if arr[j]  < maxVal:
                break
              
        # if j - i == 0 than means there is no unsorted part and ek element pr bethe h i and j
        if j - i <= 0: # if j - i < 0 that means there is no unsorted part
            return [0,0]
        
        return [i,j]