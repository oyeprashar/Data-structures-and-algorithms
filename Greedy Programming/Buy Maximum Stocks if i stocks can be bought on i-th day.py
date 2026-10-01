"""
In a stock market, there is a product with its infinite stocks. The stock prices are given for N days,
where arr[i] denotes the price of the stock on the ith day. There is a rule that a customer can buy at 
most i stock on the ith day. If the customer has an amount of k amount of money initially, find out the
maximum number of stocks a customer can buy. 

For example, for 3 days the price of a stock is given as [7, 10, 4]
You can buy 1 stock worth 7 rs on day 1, 2 stocks worth 10 rs each on day 2
and 3 stock worth 4 rs each on day 3.
"""

class Solution:
    def buyMaximumProducts(self, budget, prices):

        stocks = []

        for index, value in enumerate(prices):
            stocks.append([value, index + 1])

        stocks.sort() # smallest first because we want to maximise the count and buy alot
        stocksBought = 0

        for stock in stocks:

            value = stock[0]
            quantity = stock[1]

            # buy all if we can
            if budget - (value * quantity) >= 0:
                stocksBought += quantity
                budget -= (value * quantity)

            # cant fit in the budget? Buy the units that we can!
            else:
                stocksBought += (budget // value)
                # budget // value gives us the number of units we can buy for the current stock such that it fits our current budget

                return stocksBought

        return stocksBought




