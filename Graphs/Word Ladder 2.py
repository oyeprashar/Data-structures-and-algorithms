from collections import defaultdict

class Solution:
    
    def findPath(self,currWord,currPath,endWord,adj,ans):
                
        if currWord == endWord:
            currPath.append(currWord)
            ans.append(currPath.copy())
            currPath.pop()
            return 
        
        currPath.append(currWord)
        for nbr in adj[currWord]:
            self.findPath(nbr,currPath,endWord,adj,ans)
        currPath.pop()
        
        
        
    def findDepth(self,beginWord,endWord,wordSet):
        
        adj = defaultdict(list)
        
        queue = [beginWord]
        visited = {beginWord:0}
        count = 0
        possible = False
        
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
                        
                        if newStr in wordSet:
                            
                            if newStr not in visited:
                                queue.append(newStr)
                                visited[newStr] = visited[curr] + 1
                                adj[curr].append(newStr)\
                            
                            else:
                                if visited[newStr] == visited[curr] + 1:
                                    adj[curr].append(newStr)
                            
                    
                        if newStr == endWord:
                            possible = True
                        
                    arr[i] = orgChar
        
        # print(visited)
        return possible,adj
                
    def findLadders(self, beginWord: str, endWord: str, wordList):
        
        # step one is to find if there is a valid path
        
        wordSet = set()
        endPresent = False
        
        for word in wordList:
            
            if word == endWord:
                endPresent = True
            
            wordSet.add(word)
        
        if endPresent == False:
            return []
    
        possible,adj = self.findDepth(beginWord,endWord,wordSet)
        
        if possible == False:
            return []
        ans = []
        self.findPath(beginWord,[],endWord,adj,ans)
        
        return ans
        
            
            