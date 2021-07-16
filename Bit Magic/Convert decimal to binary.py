"""
integer is 4byte or 32 bits
"""

def convert(n):

    i = 31

    while i >= 0:
        k = n >> i 

        if k & 1 > 0:
            print("1",end="")
        else:
            print("0",end="")

        i -= 1

convert(5)
