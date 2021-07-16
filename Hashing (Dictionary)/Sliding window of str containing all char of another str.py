# abcdefgh
# agh

class Solution:
    def maximizeleftIndex(self,left,right,rightIndex,leftAns,s,substringDict):
        
        if left <= right:
            
            mid = (left + right) // 2
            
            if self.isValid(mid,rightIndex,s,substringDict) is True:
                # save the index and move to right to maximize it
                leftAns[0] = mid
                return self.maximizeleftIndex(mid+1,right,rightIndex,leftAns,s,substringDict)
            else:
                # else move to left to find a valid ans
                
                self.maximizeleftIndex(left,mid-1,rightIndex,leftAns,s,substringDict)
        else:
            return -1
                
    def minimizeRightIndex(self,left,right,rightAns,s,substringDict):
        if left <= right:
            mid = (left + right) // 2
            # print("Mid",mid,"left = ",left)
            if self.isValid(0,mid,s,substringDict) is True:
                # print("True for index",mid)
                # we save it and move to lef to minimize it!
                rightAns[0] = mid
                return self.minimizeRightIndex(left,mid-1,rightAns,s,substringDict)
            else:
                # move right to find a valid ans
                # print("False for index",mid)
                return self.minimizeRightIndex(mid+1,right,rightAns,s,substringDict)
        else:
            return -1
                
        
    def isValid(self,left,right,s,subStringDict):
        dict1 = {}
        for char in s[left:right+1]:
            dict1[char] = 0
        for char in s[left:right+1]:
            dict1[char] += 1
            
        for char in subStringDict:
            if char not in dict1:
                return False
            if dict1[char] < subStringDict[char]:
                return False
        return True
    def smallestWindow(self, s, p):
        
        subStringDict = {}
        
        for char in p:
            subStringDict[char] = 0
        for char in p:
            subStringDict[char] += 1
            
        # left=4
        # right=9
        
        left = 0
        right = len(s) - 1
        
        rightAns = [-1]
        # print(self.isValid(left,right,s,subStringDict))
        self.minimizeRightIndex(left,right,rightAns,s,subStringDict)
        rightIndex = rightAns[0]
        
        leftAns = [-1]
        right = rightIndex
        self.maximizeleftIndex(left,right,rightIndex,leftAns,s,subStringDict)
        
        leftIndex = leftAns[0] 
         
        return s[leftIndex:rightIndex+1]


s = Solution()
str1 =  "abcdefgh"
p = "agh"
print(s.smallestWindow(str1,p))