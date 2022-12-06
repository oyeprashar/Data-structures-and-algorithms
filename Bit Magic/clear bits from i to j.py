# method1
def cleariToj(num,i,j):
    maskA = -1 << (j + 1)
    maskB = (1 << i) - 1

    fMask = maskA | maskB
    return num & fMask

print(cleariToj(55,1,4))


# method2
def clear(num,i,j):

    maskA = -1 << j
    maskB = ~(-1 << (i-1))
    mask = maskA | maskB
    return num & mask

print(clear(42,2,5))
print(clear(63,1,4))