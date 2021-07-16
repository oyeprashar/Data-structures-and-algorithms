def updateBit(num,i,value):

    # if value == 1, then it means we need to set the ith bit
    if value == 1:
        mask = 1 << i
        return num | mask

    # if value == 0, then it means we need to clear the ith bit
    else:
        mask = 1 << i
        mask = ~mask
        return num & mask

print(updateBit(5,3,1))
print(updateBit(5,0,0))