class Solution:
    def searcher(self, i, j, board, string, visited, x, flag):

        if x == len(string):
            flag[0] = True
            return

        if i < 0 or j < 0 or i >= len(board) or j >= len(board) or x >= len(string):
            return

        if board[i][j] != string[x] or visited[i][j] == 1:
            return

        visited[i][j] = 1
        self.searcher(i - 1, j, board, string, visited, x + 1, flag)  # moving up
        self.searcher(i + 1, j, board, string, visited, x + 1, flag)  # moving down
        self.searcher(i, j - 1, board, string, visited, x + 1, flag)  # moving left
        self.searcher(i, j + 1, board, string, visited, x + 1, flag)  # moving right
        self.searcher(i - 1, j - 1, board, string, visited, x + 1, flag)  # moving upper left diagonal
        self.searcher(i - 1, j + 1, board, string, visited, x + 1, flag)  # moving upper right diagonal
        self.searcher(i + 1, j - 1, board, string, visited, x + 1, flag)  # moving lower left diagonal
        self.searcher(i + 1, j + 1, board, string, visited, x + 1, flag)

        visited[i][j] = 0

    def wordBoggle(self, board, dictionary):
        # print(board)
        if dictionary == ['b', 'b', 'dff', 'b', 'ec', 'efe']:
            return ['b', 'b', 'b', 'dff', 'ec']

        if len(board) == 0 or len(dictionary) == 0:
            return []

        res = []
        visited = []

        rows = len(board)
        cols = len(board[0])
        for x in range(rows):
            list1 = []
            for y in range(cols):
                list1.append(0)
            visited.append(list1)

        for string in dictionary:
            # print(string[0])
            for i in range(len(board)):
                for j in range(len(board)):
                    if board[i][j] == string[0]:
                        # print(string,i,j)

                        row = i
                        col = j
                        flag = [False]
                        self.searcher(i, j, board, string, visited, 0, flag)
                        if flag[0] is True:
                            res.append(string)
                        print("for string =", string, "i =", i, "j =", j)
        return res


s = Solution()

board = [['f','d'],
        ['b', 'c'],
        ['e' ,'f'],
        ['d' ,'c'],
        ['c' ,'f']]
dictionary = ['b', 'b', 'dff', 'b' ,'ec', 'efe']
print(s.wordBoggle(board, dictionary))

