# TIME COMPLEXITY : O(n^2) | SPACE COMPLEXITY : O(n)
def getCatalanNum(n):

    if n == 0:
        return 1

    memory = [0] * (n+1)
    memory[0] = 1
    memory[1] = 1

    for x in range(2,n+1):
        ans = 0
        for i in range(1,x+1):
            ans += memory[i-1] * memory[x-i]

        memory[x] = ans

    return memory[n]

print(getCatalanNum(5))


def catalan(n,memory):

    if n == 0 or n == 1:
        return 1
    
    if memory[n] != -1:
        return memory[n]
    
    curr = 0
    for i in range(1,n+1):
        curr += (catalan(i-1,memory) * catalan(n-i,memory)) 

    memory[n] =  curr
    return memory[n]

def getCatalan(n):
    memory = [-1] * (n+1)
    return catalan(n,memory)