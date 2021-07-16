# TIME COMPLEXITY : O(n^2) | SPACE COMPLEXITY : O(n)

def uniqueBST(n):
    memory = [0] * (n+1)
    memory[0] = 1
    memory[1] = 1

    for x in range(2,n+1):
        ans = 0
        for i in range(1,x+1):
            ans += memory[i-1]*memory[x-i]

        memory[x] = ans

    return memory[n]


print(uniqueBST(5))