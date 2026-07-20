
# [[C, A, P], [A, N, D], [T, I, E]], dictionary[] = ["CAT"]
class Solution:


    def wordBoggleHelper(self, i, j, board, currIndex, currWord, visited, directions):

        if currIndex[0] == len(currWord):
            return True

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or currIndex[0] > len(currWord):
            return False

        if visited[i][j] is True or board[i][j] !=  currWord[currIndex[0]]:
            return False

        visited[i][j] = True
        currIndex[0] += 1

        for dir in directions:
            if self.wordBoggleHelper(i + dir[0], j + dir[1], board, currIndex, currWord, visited, directions):
                visited[i][j] = False
                return True

        currIndex[0] -= 1
        visited[i][j] = False


    def wordBoggle(self, board, dictionary):

        directions = [ (-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visited = []
        for i in range(len(board)):
            currRow = []
            for j in range(len(board[0])):
                currRow.append(False)
            visited.append(currRow)

        ans = []

        for i in range(len(board)):
            for j in range(len(board[0])):

                for word in dictionary:

                    if word[0] == board[i][j]:

                        currIndex = [0]
                        if self.wordBoggleHelper(i, j, board, currIndex, word, visited, directions):

                            ans.append(word)

        return list(set(ans))




s = Solution()
mat = [["C", "A", "P"], ["A", "N", "D"], ["T", "I", "E"]]
print(s.wordBoggle(mat, ["CAT"]))

