"""
"""
def winesSolver(wines):
    # Step1: Initialize all cells with 0
    memory = []
    for x in range(len(wines)):
        list1 = []
        for y in range(len(wines)):
            list1.append(0)
        memory.append(list1)

    # Step2: Fill the principal diagonal (year is always the last for the principal diagonal)
    for n in range(len(wines)):
        memory[n][n] = wines[n] * (len(wines))
    # Step3: Fill all the diagonals with start at row = 0 and col = 1 till len(wines)-1
    for j in range(1, len(wines)):  # len(wines) will not be included, it will go till len(wines)-1
        row = 0
        col = j
        while col < len(wines):
            year = len(wines) - abs(row - col)
            op1 = wines[row] * year + memory[row + 1][col]
            op2 = wines[col] * year + memory[row][col - 1]
            memory[row][col] = max(op1, op2)
            col += 1
            row += 1

    for list2 in memory:
        print(list2)
    return memory[0][len(wines) - 1]


wines = [2, 3, 5]
print(winesSolver(wines))
