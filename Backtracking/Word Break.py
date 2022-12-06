class Solution:
    
    def isValid(self,currWord,dict1):
        if currWord in dict1:
            return True
        return False
    
    def generateWords(self,start,curr,string,dict1,ans):
    
        if start == len(string):
            currStr = " ".join(curr)
            ans.append(currStr)
            return 
    
        for end in range(start,len(string)):
    
            currWord = string[start:end+1]
    
            if self.isValid(currWord,dict1) == True:
                curr.append(currWord)
                self.generateWords(end+1,curr,string,dict1,ans)
                curr.pop() 
        
    def wordBreak(self, n, dict1, string):
        
        start = 0
        curr = []
        ans = []
        self.generateWords(start,curr,string,dict1,ans)
        return ans