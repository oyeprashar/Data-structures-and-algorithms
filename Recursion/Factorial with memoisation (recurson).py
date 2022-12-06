######## Recursion practice ########

factorial_memo = {} ## Dictionary is made 

def factorial(k):
    
    if k == 0: ##  since 0! = 1
        return 1
    
    if not k in factorial_memo:    ## if input k is not in our dictionary, add it in our dictionary
        factorial_memo[k] = k * factorial(k-1)
       
        
    return factorial_memo[k] ## return the value from dictionary using the key k which is inputed by our user

print(factorial(4))