class Solution:
    def longestPalindrome(self, string: str) -> str:
        
        
        if len(string) == 1:
            return string
        
        if len(string) == 2:
            if string == string[::-1]:
                return string
            else:
                return string[0]
        
        maxLen = 1
        indices = [-1,-1]

        memory = []
        for x in range(len(string)):
            list1 = []
            for y in range(len(string)):
                list1.append(0)
            memory.append(list1)

        for index in range(len(string)):
            maxLen = 1
            indices[0] = index
            indices[0] = index
            memory[index][index] = 1

        x  = 0
        y = 1



        while y < len(string):
            if string[x] == string[y]:
                currLen = (y-x) +1

                if currLen > maxLen:
                    maxLen = currLen
                    indices[0] = x
                    indices[1] = y

                memory[x][y] = 1

            x += 1
            y += 1

        # formula :- if string[i] == string[j] and string[i+1] == string[j-1] ==> we have a palindrome from i till j

        starti = 0
        startj = 2

        while startj < len(string):
            i = starti
            j = startj

            while i < len(string) and j < len(string):
                if string[i] == string[j] and memory[i+1][j-1] == 1:
                    currLen = (j-i) + 1
                    if currLen > maxLen:
                        maxLen = currLen
                        indices[0] = i
                        indices[1] = j

                    memory[i][j] = 1

                i += 1
                j += 1

            startj += 1

        start = indices[0]
        end = indices[1]

        ans = string[start:end+1]
       

        return ans