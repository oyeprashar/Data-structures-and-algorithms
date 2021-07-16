"""
==== Moore voting algorithm ====
-> It is used to find a candidate with occurencs > len(arr) // 2

->Why is this algo used?
Because it find the majority element in o(n) time and just O(1) space, having a dictionary or hashmap will work in O(n) time but it will also use O(n) space

->Draw back of Moore voting algorithm?
It only works when we need to find an element occuring for more than len(arr) // 2 times. 
Note: MORE THAN len(arr) // 2 NOT EQUAL!
"""

class Solution:
    def majorityElement(self, A, N):
        candidate = A[0]
        count = 1
    
        # step1: Find a candidate
        for i in range(1,len(A)):
            num = A[i]
            
            if num == candidate:
                count += 1
            else:
                count -= 1
                if count == 0:
                    candidate = num
                    count = 1
        # step2: Verify the candidate
        count = 0
        for num in A:
            if num == candidate:
                count +=1 
        
        if count > len(A) // 2:
            return candidate
        else:
            return -1   