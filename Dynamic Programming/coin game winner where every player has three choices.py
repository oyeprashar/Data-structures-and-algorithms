def canAWin(n,x,y):

    arr = [False] * (n+1)
    arr[1] = True

    for i in range(2,n+1):
        if n - 1 >= 0 and arr[n -1] == False:
            arr[n] = True 
        
        elif n - x >= 0 and arr[n - x] == False:
            arr[n] = True 
        
        elif n - y >= 0 and arr[n - y] == False:
            arr[n] = True 
        
    
    return arr[n]

def findWinner(n,x,y):

    isAWinner = canAWin(n,x,y)

    if isAWinner == True:
        return "A"
    else:
        return "B"
    
x = 3
y = 4
n = 6

print("The winner is",findWinner(n,x,y))