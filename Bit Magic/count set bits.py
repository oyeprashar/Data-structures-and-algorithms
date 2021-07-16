"""
Count the number of set bits
This can count the number of set bits even in negative numbers
"""

def countSetBits(num):

    i = 31
    ans = 0

    while i >= 0:
        k = num >> i 
        if k & 1 > 0:
            ans += 1
        i -= 1

    return ans

print(countSetBits(-5))

