"""
This DOESNT NOT work with negative numbers
"""
def convert2Binary(num):
    p = 1
    sum = 0
    while num > 0:
        curr = num & 1
        sum += curr*p

        num = num >> 1
        p *= 10

    return sum

print(convert2Binary(5))
# for i in range(0,101):
#     print(convert2Binary(2**i))