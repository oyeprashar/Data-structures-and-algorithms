"""
we use a word from a row and then move ahead to the next row to generate the combinations
"""

def printRec(currRowIndex, mat, currString):

    if currRowIndex == len(mat):
        print(currString)
        return

    for col in range(len(mat[currRowIndex])):
        printRec(currRowIndex + 1, mat, currString + " " + mat[currRowIndex][col])


def printCombinations(mat):
    printRec(0, mat, "")


printCombinations([
    ["you", "we"],
    ["have", "are"],
    ["sleep", "eat", "drink"]])


