def clearBit(num,i):
    mask = 1 << i
    mask = ~mask
    return num & mask

print(clearBit(25,0))