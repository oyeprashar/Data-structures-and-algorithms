class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        endPresent = False
        wordSet = set()
        
        for word in wordList:
            
            if word == endWord:
                endPresent = True
            
            wordSet.add(word)
        
        if endPresent == False:
            return 0
    
        queue = [beginWord]
        count = 0
        visited = set()
        visited.add(beginWord)
        
        while len(queue) > 0:
            
            count += 1
            size = len(queue)
            
            for _ in range(size):
                
                curr = queue.pop(0)
                
                arr = [char for char in curr]
                
                for i in range(len(arr)):
                    orgChar = arr[i]
                    
                    for j in range(ord('a'),ord('z')+1):
                        newChar = chr(j)
                        
                        arr[i] = newChar
                        newStr = "".join(arr)
                        
                        # if the new newStr is in the wordSet and it is not visited already then add it to the queue
                        if newStr in wordSet and newStr not in visited:
                            queue.append(newStr)
                            visited.add(newStr)
                            
                        arr[i] = orgChar
                        
                        if newStr == endWord:
                            return count + 1
                        
        return 0