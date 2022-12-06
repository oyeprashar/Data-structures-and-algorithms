# If we have an amount n and coins of value listed in coins=[], we have to return min number of coins we can use to 
# represent that amount n 

def coin_change(n,coins):
	# we have set min_coins to n just to compare count with min_coins and return it
	min_coins = n

	# base condition
	if n in coins:
		return 1

	else: 
		# list comprehension which coins having value less then or equal to our given value and we are looping thro this list
		for i in [c for c in coins if c <=n]: 

			count = 1 + coin_change(n-i, coins) #important

			if count < min_coins:
				min_coins = count # resetting our min_coins
	return min_coins

coins = [1,5,10,25]
print(coin_change(16,coins))

