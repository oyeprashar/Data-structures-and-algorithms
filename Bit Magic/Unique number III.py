"""
Find the unique number that appears exactly once while other numbers appears exactly thrice
"""

def findUnique(array):
    resArray = [0] * 64

    for num in array:
        pos = 0

        while num != 0:
            if num & 1 == 1:
                resArray[pos] += 1
            pos += 1
            num = num >> 1

    res = 0
    for i in range(len(resArray)):
        resArray[i] = resArray[i] % 3
        if resArray[i] == 1:
            res += 2**i
    return res

array = [3,3 ,2 ,1 ,1 ,1 ,3]
print(findUnique(array))