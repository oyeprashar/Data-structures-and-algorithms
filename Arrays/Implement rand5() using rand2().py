def rand2():
    pass

def rand5():
    num = 4*rand2() + 2 * rand2() + rand2()

    if num == 5:
        return rand5()
    
    return num 