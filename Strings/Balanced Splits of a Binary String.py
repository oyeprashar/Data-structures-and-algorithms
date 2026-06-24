"""
A string is given which is made up of 0s and 1s. We need to find the ways we can split the strings into subsequences such that
0s and 1s are balanced and we need to split the whole string. If the complete string cannot be split in such a manner, we return
-1. 
"""

class Solution:
    def maxSubStr(self, string):
        
        countZero = 0
        countOne = 0
        totalSplit = 0
        
        for i in range(len(string)):
            
            if string[i] == "0":
                countZero += 1
                
            elif string[i] == "1":
                countOne += 1
                
            if countZero != 0 and countOne == countZero:
                totalSplit += 1
                countOne = 0
                countZero = 0
                
        # This means, there is unbalanced part and the whole string cannot be split!         
        if countOne != countZero:
            return -1
        
        return totalSplit
                
