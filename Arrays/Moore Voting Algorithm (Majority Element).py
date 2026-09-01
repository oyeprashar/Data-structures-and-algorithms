"""
==== Moore voting algorithm ====
-> It is used to find a candidate with occurencs > len(arr) // 2

->Why is this algo used?
Because it finds the majority element in o(n) time and just O(1) space, having a dictionary or hashmap will work in O(n)
time, but it will also use O(n) space

->Draw back of Moore voting algorithm?
It only works when we need to find an element occuring for more than len(arr) // 2 times. 
Note: MORE THAN len(arr) // 2 NOT EQUAL!

    Explanation of why it works :

    arr = [2, 2, 1, 1, 1, 2, 2]

    When we run the algo the following happens because of the way we are counting :
        2 cancels 1
        2 cancels 1
        1 cancels 2

    There are not enough elements to cancel and remove the majority from the candidate and because of that the
    algo works
"""

class Solution:
    def majorityElement(self, arr):

        """
        The majority element is the one that is present more than n/2
        """

        # step 1 : We need to find a candidate element that can possibly be the majority element
        candidate = arr[0]
        count = 1

        for i in range(1, len(arr)):

            if arr[i] == candidate:
                count += 1

            else:
                count -= 1

            if count == 0:
                candidate = arr[i]
                count = 1

        # step 2 : We then run a loop to verify that this element is indeed the majority
        verificationCount = 0
        for element in arr:
            if element == candidate:
                verificationCount += 1

        if verificationCount > len(arr) // 2:
            return candidate

        return -1
