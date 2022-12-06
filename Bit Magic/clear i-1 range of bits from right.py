# bits are cleared till position i -1 and i number of bits are cleared
def clearRange(num,i):
    mask = -1 << i
    return num & mask

print(clearRange(25,4))