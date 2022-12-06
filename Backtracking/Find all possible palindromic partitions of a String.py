class Solution:
    def isPalindrome(self,string):
        return string == string[::-1]
        
    def findPartitions(self,start,curr,ans,string):
        if start >= len(string):
            currS = curr.copy() # we have to copy because the original curr is being back tracked and ans me agar same daalengye 
            ans.append(currS)   # toh dono same memory reference karne lagengye aur dono back track ho jayengye! But we want to save the ans
            return 
        
        for end in range(start,len(string)):
            if self.isPalindrome(string[start:end+1]) is True:
                curr.append(string[start:end+1])
                self.findPartitions(end+1,curr,ans,string)
                curr.pop()
        
            
        
    def allPalindromicPerms(self, S):
        ans = []
        curr = []
        start = 0
        string = S
        self.findPartitions(start,curr,ans,string)
        return ans

s = Solution()
string = "geeks"
print(s.allPalindromicPerms(string))