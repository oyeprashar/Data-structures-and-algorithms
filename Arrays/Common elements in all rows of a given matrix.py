
def findCommonElement(mat):

    freq = {}



    for i in range(len(mat)):

        # step 1 : convert each row to a set to keep everything unique (since elements can repeat in a row)
        currRowSet = set(mat[i])

        # step 2 : Add it to the freq dict
        for element in currRowSet:
            if element in freq:
                freq[element] += 1
            else:
                freq[element] = 1

    # step 3 : save the elements that repeat in all the rows
    res = []
    for element in freq:
        if freq[element] == len(mat):
            res.append(element)

    return res

mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]


print(findCommonElement(mat))
