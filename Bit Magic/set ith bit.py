def setBit(num,i):
    mask = 1 << i
    return num | mask

print(setBit(5,1))