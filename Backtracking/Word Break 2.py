"""
Approach :

    Core logic:
        - We start from an index and start forming words using a look that runs from current index till the end of the
          word. These recursive calls ensures that we are exploring all the possible combinations.

        - The logic returns back all the sentences we can form using the current word as the prefix.

        - If the word itself is the complete sentence (last word in recursions stack) then it returns back [""] and we
          do not add empty space after this

    Memoization logic :
        - Simply save the sentences based on the currIndex and reuse them


    Time complexity analysis :
        - In this problem we need to make the sentences and return them.
        - We have two choices are each index, put a blank space (break) or dont
        - We need to form the word as well to check if its in the dict
        - TC = O(2^n * n)

"""



class Solution:

    def generateWords(self, currIndex, string, dict, cache):

        # base case
        if currIndex == len(string):
            return [""]

        if currIndex in cache:
            return cache[currIndex]

        sentences = []

        # since we are running a loop, we will explore wll the possible combinations starting fro the current word
        for i in range(currIndex, len(string)):

            currWord = string[currIndex: i + 1]

            if currWord in dict:

                remainingSentences = self.generateWords(i + 1, string, dict, cache)
                for sentence in remainingSentences:

                    if sentence == "":
                        sentences.append(currWord)

                    else:
                        sentences.append(currWord + " " + sentence)

        cache[currIndex] = sentences
        return cache[currIndex]

    def wordBreak(self, dictionary, string):
        dict = set(dictionary)
        cache = {}
        self.generateWords(0, string, dict, cache)
        return cache[0]