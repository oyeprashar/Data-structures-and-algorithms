def maxProfitWinesSolver(i,j,year,wines,memory):
    if i > j:
        return 0

    if memory[i][j] != 0:
        print("accesing memory for:", i, j)
        return memory[i][j]

    op1 = wines[i] * year + maxProfitWinesSolver(i+1,j,year+1,wines,memory)
    op2 = wines[j] * year + maxProfitWinesSolver(i,j-1,year+1,wines,memory)

    res = max(op1,op2)
    print("computing for:",i,j)
    memory[i][j] = res

    return res


# wines = [2,3,5]
wines = [2,3,5,1,4]

# building the memory matrix
memory = []
for x in range(len(wines)):
    list1 = []
    for y in range(len(wines)):
        list1.append(0)
    memory.append(list1)

year = 1
i = 0
j = len(wines)-1
print(maxProfitWinesSolver(i,j,year,wines,memory))