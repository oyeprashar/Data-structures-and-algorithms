"""
We need to count number of triplets whose sum is less than the given target 

-> We use a single loop to find the first number 
-> We use two pointer method to find left and right index jaha sum of arr[i] + arr[left] + arr[right] < target 
-> if less aata hai toh right - left number of pairs can be made with i
-> increment the left pointer
-> else increment the right pointer


"""
class Solution:
    def countTriplets(self, arr, n, sumo):
        arr.sort() # our two pointer method works on sorted array
        count = 0
        
        
        for i in range(len(arr)-2):
            # we need to find a pair of nums such that i + arr[left] + arr[right] < target
            left = i+1
            right = len(arr)-1
            
            while left < right:
                
                if arr[i] + arr[left] + arr[right] < sumo:
                    count += right - left  # if left and right waala range sahi h toh element from left to right will form pair with the arr[i]
                    left += 1                              
                else:
                    right -= 1
        
        return count
            