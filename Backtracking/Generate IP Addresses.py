class Solution:
    
    def isValid(self,currChunk,startIndex):

        if len(currChunk) == 0:
            return False

        if currChunk[0] == "0" and len(currChunk) > 1: 
            return False 

        currChunk = int(currChunk)

        if currChunk < 0 or currChunk > 255:
            return False 

        return True 
    
    def generateIP(self,currIndex,curr,string,ans,count):

        if len(curr) > 4:
            return  

        if  currIndex == len(string) and len(curr) == 4:
            currIP = ".".join(curr)
            ans.append(currIP)
            return  

        for end in range(currIndex,currIndex+3):

            currChunk = string[currIndex:end+1]

            if self.isValid(currChunk,currIndex) == True:
                curr.append(currChunk)
                self.generateIP(end+1,curr,string,ans,count + 1)
                curr.pop()

    def restoreIpAddresses(self, s):
        
        ans = []
        self.generateIP(0,[],s,ans,0)
        return ans 