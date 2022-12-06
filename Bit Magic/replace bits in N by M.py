"""
replace bits in N by M
-> The indices starts from 1 in the GFG problem
-> first we need to clear bits from i to j in N
-> left shift M by i
-> do bitwise OR of N and M
"""

def clearBitsFromiToj(num,i,j):
    maskA = -1 << (j + 1)
    maskB = (1 << i) - 1
    fMask = maskA | maskB

    return num & fMask

def replace(N,M,i,j):
    N = clearBitsFromiToj(N,i,j)
    return N | (M<<i)

print(replace(15,2,1,3))














