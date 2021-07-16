"""
integer is 4byte or 32 bits
This works for negative numbers too!
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

# orignal number = 2 4
# maskA = -16 maskB = 1
# final mask = -15 n after and with mask = 0 m after i-1 left shift = 8
# 8

convert(4)
print()
convert(2)
print()
convert(2)
print()
print("========================================================")
convert(6)
print()
convert(3)
print()
convert(2)
