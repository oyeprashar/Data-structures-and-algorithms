"""
        Input: mat = [[0,1,1,1],
                      [0,0,1,1],
                      [1,1,1,1],
                      [0,0,0,0]]

        Since the rows are sorted, in the row with max numbers of 1, 1 will appear the at the min index among all the rows
        """

class Solution:
    def rowWithMax1s(self, mat):
        
        smallest_col = 3 ** 38
        max_ones_row_index = -1
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                # we found first one in this row. Save the index and move on to next row
                if mat[i][j] == 1:
                    if j < smallest_col:
                        smallest_col = j
                        max_ones_row_index = i
                    break

        return max_ones_row_index
