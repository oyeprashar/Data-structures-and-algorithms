# creating a list of values to work on
num1  = [7,21,18,3,12]
n = max(num1)
#creating list of all true values to change later
prime = [True for i in range(n+1)]
print(prime)
p = 2 # starting with the first known prime number
while(p*p <= n): 
    if prime[p] == True:
        for i in range(p*p, n+1, p): # changing values for composite num to false
            prime[i] = False
    p = p + 1

for i in num1:   # checking the values we need from the list of all values till n
    if prime[i] == True:
        print(f"Prime = {i}")
    else:
        print(f"Composite = {i}")