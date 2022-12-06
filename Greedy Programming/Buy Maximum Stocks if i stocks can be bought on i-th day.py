"""
In a stock market, there is a product with its infinite stocks. The stock prices are given for N days,
where arr[i] denotes the price of the stock on the ith day. There is a rule that a customer can buy at 
most i stock on the ith day. If the customer has an amount of k amount of money initially, find out the
maximum number of stocks a customer can buy. 

For example, for 3 days the price of a stock is given as [7, 10, 4]
You can buy 1 stock worth 7 rs on day 1, 2 stocks worth 10 rs each on day 2
and 3 stock worth 4 rs each on day 3.
"""
#price = [ 10, 7, 19 ] k = 45

def maxCount(input_arr,capacity):

    arr = []
    for index,value in enumerate(input_arr):
        
        arr.append([value,index+1])
    
    arr.sort()

    count = 0

    for stock in arr:
        
        if stock[0]*stock[1] <= capacity: # stock * day
            
            capacity -= stock[0]*stock[1]
            count += stock[1]
            print("taking ==",stock[0]*stock[1],"capacity ==",capacity,"count ==",count)
        
        else:
            canBuy = min(capacity // stock[0], stock[1])
            count += canBuy 
            capacity -= (canBuy * stock[1])
            print("taking ==",canBuy * stock[1],"capacity ==",capacity,"count ==",count)
        
    return count

arr = [ 10, 7, 19 ]
print(maxCount(arr,45))




