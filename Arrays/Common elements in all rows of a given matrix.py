"""
mat[4][5] = {{1, 2, 1, 4, 8},
             {3, 7, 8, 5, 1},
             {8, 7, 7, 3, 1},
             {8, 1, 2, 7, 9},
            };

"""

def findCommonElement(mat):

    freq = {}

    for i in range(len(mat)):

        currRow = set()
        for j in range(len(mat[0])):

            currEle = mat[i][j] 

            # unique elements of current row goes to freq dict
            if currEle not in currRow:
                if currEle not in freq:
                    freq[currEle] = 1
                
                else:
                    freq[currEle] += 1
            
                currRow.add(currEle) 
        
    common = []

    for num in freq:
        if freq[num] == len(mat):
            common.append(num)
        
    return common
        
mat = [[1, 2, 1, 4, 8],
    [3, 7, 8, 5, 1],
    [8, 7, 7, 3, 1],
    [8, 1, 2, 7, 9]]   
                
print(findCommonElement(mat))

