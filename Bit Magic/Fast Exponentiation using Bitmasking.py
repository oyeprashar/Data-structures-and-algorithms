def exp(num,powerNumber):
    ans = 1

    while powerNumber != 0:
        if powerNumber & 1 == 1:
            ans = ans * num
        num = num * num
        powerNumber = powerNumber >> 1

    return ans


print(exp(10,3))

