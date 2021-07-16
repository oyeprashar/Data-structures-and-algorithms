def isValid(board,row,col):
    rowH = row-1
    while rowH > -1:
        if board[rowH][col] == 1:
            return False
        rowH -= 1

    ldRow = row-1
    ldCol = col-1
    while ldRow >= 0 and ldCol >= 0:
        if board[ldRow][ldCol] == 1:
            return False
        ldRow -= 1
        ldCol -= 1

    rdRow = row-1
    rdCol = col+1
    while rdRow >= 0 and rdCol < len(board):
        if board[rdRow][rdCol] == 1:
            return False
        rdRow -= 1
        rdCol += 1

    return True


def Nqueens(board,row,res):

    if row == len(board):
        list1 = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    list1.append(j+1)
        res.append(list1)
        return


    for col in range(len(board)): # row ke har column ko check krna h
        if isValid(board,row,col) is True: # ex call1 -> call2 -> call3 not valid, so no more further calls are made and hence it will start to return back
            board[row][col] =  1           # call1 - > call2 -> if row == len(board) save ans and return
            Nqueens(board,row+1,res)
            board[row][col] = 0



    # return
#
board =[[0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0]]
# board = [[0]]
res = []
Nqueens(board,0,res)
print(res)
# print(board)
