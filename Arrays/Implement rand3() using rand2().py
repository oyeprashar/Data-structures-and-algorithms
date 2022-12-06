def rand2():
    pass

def rand3():

    num = 2 * rand2() + rand2()

    if num == 3:
        return rand3()
    
    return num 

