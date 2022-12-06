class Solution:
    def isPossible(self,currIndex,string,wordDict,memory):


        if currIndex == len(string):
            return True

        if memory[currIndex] != -1:
            return memory[currIndex]

        for end in range(currIndex,len(string)):
            currWord = string[currIndex:end+1]

            if currWord in wordDict and self.isPossible(end+1,string,wordDict,memory) == True:
                memory[end] = True
                return True

        memory[currIndex] = False
        return False

    def wordBreak(self, string: str, wordDict: List[str]) -> bool:
        
        wordDict = set(wordDict)
        memory = [-1] * len(string)
        return self.isPossible(0,string,wordDict,memory)