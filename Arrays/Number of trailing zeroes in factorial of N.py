
def trailingZeroes(N):
    
	x = 5
	count = 0
	
	while N // x > 0:
	    count += (N // x) 
	    x *= 5
	return count

print(trailingZeroes(5)) # 5! = 120, we have 1 trailing zeroes
print(trailingZeroes(3)) # 3! = 6, we have 0 trailing zeroes

