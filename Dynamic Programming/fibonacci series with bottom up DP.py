"""
In bottom up DP we dont use recursion, we use a single loop and build the ans
TIME COMPLEXITY = O(N) | SPACE COMPLEXITY = O(N)
"""

def fib(n,arr):

    for i in range(2,n+1):

        arr[i] = arr[i - 1] + arr[i - 2]


    return arr[n]

n = 6
arr = [-1] * (n+1)
arr[0] = 0
arr[1] = 1
print(fib(n,arr))

"""
Reducing the space complexity from O(N) to O(1) 
"""

def fib_S_OPTIMIZED(n,a,b,c):

    for i in range(2,n+1):
        c = a + b
        a = b
        b = c

    return c

print(fib_S_OPTIMIZED(5,0,1,1))

