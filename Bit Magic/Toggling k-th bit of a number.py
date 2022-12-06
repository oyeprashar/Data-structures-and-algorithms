
def findKthBit(num,k):
    mask = 1 << (k-1)

    if num & mask > 0:
        return 1
    else:
        return 0

def update(num,i,value):

    if value == 1:
        mask = 1 << (i-1)
        return num | mask

    if value == 0:
        mask = 1 << (i-1)
        mask = ~mask

        return num & mask

def toggle(num,k):
    if findKthBit(num,k) == 1:
        return update(num,k,0)
    else:
        return update(num,k,1)


print(toggle(75,4))
