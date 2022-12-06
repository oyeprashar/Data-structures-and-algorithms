"""
if k > n:
    p(n,k) == 0 
else:
    p(n,k) == n! / (n-k)!
"""

def factorialHelper(n,memory):

    if n == 0 or n == 1:
        return 1 
    
    if memory[n] != -1:
        return memory[n]
    
    memory[n] = n * factorialHelper(n-1,memory)
    return memory[n]

def factorial(n):
    memory = [-1] * (n+1)
    return factorialHelper(n,memory)

def p(n,k):
    if k > n:
        return 0

    numerator = factorial(n)
    denominator = factorial(n-k)

    return numerator / denominator



print(p(10, 2)) # 90
print(p(10, 3)) # 720
print(p(10, 0)) # 1
print(p(10, 1)) # 10
print(p(10,100)) # 0




