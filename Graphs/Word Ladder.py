"""
Time complexity analysis :
    - let N be the number of words
    - let L be the len of the word (len is same for the words)

"""


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = [beginWord]
        levels = 0
        visited = set()
        visited.add(beginWord)

        # O(N * L * L) = O(N * L^2)
        # This will run N times
        while len(queue) > 0:

            levels += 1

            for _ in range(len(queue)):

                currWord = queue.pop(0)
                currWordList = list(currWord)

                # This will run L times
                for i in range(len(currWordList)):

                    for j in range(ord('a'), (ord('z') + 1)):

                        newChar = chr(j)
                        orgChar = currWordList[i]
                        currWordList[i] = newChar

                        # This is O(L) as well
                        newWord = "".join(currWordList)

                        if newWord in wordSet and newWord not in visited:
                            queue.append(newWord)
                            visited.add(newWord)

                        if newWord == endWord:
                            return levels + 1

                        currWordList[i] = orgChar

        return 0
