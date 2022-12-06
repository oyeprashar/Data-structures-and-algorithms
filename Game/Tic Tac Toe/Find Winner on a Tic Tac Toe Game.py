class Solution:
    
    def tictactoe(self, moves: List[List[int]]) -> str:
        
        grid = []
        count = 0
        for x in range(3):
            list1 = []
            for y in range(3):
                list1.append("1")
            grid.append(list1)
        
        flag = False

        rows = [0,0,0]
        cols = [0,0,0]
        mainDia = 0
        otherDia = 0

        for coordinates in moves:
            count += 1
            i = coordinates[0]
            j = coordinates[1]
            
            if flag == False:
                grid[i][j] = "X"
                rows[i] += ord("X")
                cols[j] += ord("X")

                if i == j:
                    mainDia += ord("X")

                if i == 0 and j == 2 or i == 1 and j == 1 or i == 2 and j == 0:
                    otherDia += ord("X")

                flag = True
            
            else:
                grid[i][j] = "O"
                rows[i] += ord("O")
                cols[j] += ord("O")

                if i == j:
                    mainDia += ord("O")

                if i == 0 and j == 2 or i == 1 and j == 1 or i == 2 and j == 0:
                    otherDia += ord("O")

                flag = False


        targetX = 3 * ord("X")
        targetO = 3 * ord("O")

        for row in rows:
            if row == targetX:
                return "A"
            if row == targetO:
                return "B"

        for col in cols:
            if col == targetX:
                return "A"
            if col == targetO:
                return "B"

        if mainDia == targetX:
            return "A"
        if mainDia == targetO:
            return "B"
        
        if otherDia == targetX:
            return "A"
        if otherDia == targetO:
            return "B"
        
        if count < 9:
            return "Pending"
        
        return "Draw"
        
        