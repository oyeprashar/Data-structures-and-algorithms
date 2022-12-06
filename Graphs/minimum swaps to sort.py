class Solution:
    def minSwaps(self, input_arr):
        arr = []

        for index,value in enumerate(input_arr):
            arr.append([value,index])
    
        arr.sort()
        count = 0
    
        for i in range(len(arr)):
    
            while arr[i][1] != i:

                oldIndex = arr[i][1]
                arr[i],arr[oldIndex] = arr[oldIndex],arr[i]
                count += 1
            
        return count


        