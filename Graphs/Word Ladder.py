class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        
        wordSet = set()
        endPresent = False

        for word in wordList:
            if word == endWord:
                endPresent = True 
            wordSet.add(word)

        if endPresent == False:
            return 0 

        count = 0
        queue = [beginWord]
        visited = set()
        visited.add(beginWord)

        while len(queue) > 0:

            size = len(queue)
            count += 1

            for _ in range(size):

                str1 = queue.pop(0)
                arr = [char for char in str1]

                for i in range(len(arr)):
                    for j in range(ord('a'),ord('z')+1):

                        newChar = chr(j)
                        orgChar = arr[i]
                        arr[i] = newChar
                        newStr = "".join(arr)
                        
                        if newStr == str1:
                            continue
                        
                        if newStr == endWord:
                            # plus one because we want to include the begin word
                            return count + 1
                        
                    
                        if newStr in wordSet and newStr not in visited:
                            queue.append(newStr)
                            visited.add(newStr)

                        arr[i] = orgChar

        # if we were not able to travese from the begin word to the end word as per the logic               
        return 0