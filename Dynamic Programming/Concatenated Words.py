class Solution:
    
    def isPossible(self,currIndex,word,wordDict,memory):
        
        if currIndex == len(word):
            return True
        
        if currIndex in memory:
            return memory[currIndex]
        
        for end in range(currIndex,len(word)):
            currWord = word[currIndex:end+1]
            
            if currIndex == 0 and end == len(word)-1:
                continue
            
            if currWord in wordDict and self.isPossible(end+1,word,wordDict,memory) == True:
                memory[currIndex] = True
                return True
            
        memory[currIndex] = False
        return False
            
        
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]: 
        
        
        wordDict = set(words)
        ans = []
        
        
        for word in wordDict:
            
            if len(word) > 0:
                memory = {}        
                if self.isPossible(0,word,wordDict,memory)== True:
                    ans.append(word)
        
            
        return ans
        