def getithBit(num,i):
    mask = 1 << i

    if num & mask >= 1:
        return 1
    return 0

print(getithBit(5,1))
