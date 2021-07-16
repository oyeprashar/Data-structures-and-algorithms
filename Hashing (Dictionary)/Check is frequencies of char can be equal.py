#User function Template for python3
class Solution:
    def isEqual(self,dictionary):
        prev = None
        for key in dictionary:
            if prev is None:
                prev = dictionary[key]
                continue
            curr = dictionary[key]
            if prev != curr:
                return False
            prev = curr
            return True
            
            
    def sameFreq(self, s):
        
        
        
        dict1 = {}
        for char in s:
            dict1[char] = 0
            
        for char in s:
            dict1[char] += 1
        
        if self.isEqual(dict1) is True:
            return False # no need to remove any character,is all ready fine!
        for key in dict1:
            dict1[key] -= 1
            if self.isEqual(dict1) is True:
                return True
            
            dict1[key] += 1
        return False
            
s = Solution()
if s.sameFreq("ababab") is True:
    print(1)
else:
    print(0)