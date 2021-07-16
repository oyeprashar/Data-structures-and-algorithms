# If we have an amount n and coins of value listed in coins=[], we have to return min number of coins we can use to 
# represent that amount n 
def coin_change(n,coins,known_results):
	 min_coins = n

	 if n in coins:
	 	known_results[n] = 1
	 	return 1
	 # checking known_results
	 elif known_results[n] > 0:     #since we initialised the whole list with zeros (no of zeros: n+1), if element is not zero it must a 
	 		return known_results[n]	# value we solved earlier and saved it to known_results[n]


	 else:
	 	for i in [c for c in coins if c<=n]:
	 		count = 1 + coin_change(n-i,coins,known_results)
	 		if count < min_coins:
	 			min_coins = count
	 			# print(known_results)
	 			known_results[n] = min_coins

	 return min_coins

coins = [1,2,3]
n = 4
# we are initialising it with n+1 zeroes because if n = 5  it will be stored at known_results[5] and since index starts with 0 to n-1 and
# agar hum n zeroes daalte toh n-1 index max hota toh fir index will be 0,1,2,3,4 and idex 5 would be out of range
known_results = [0]*(n+1) 
print(coin_change(n,coins,known_results))