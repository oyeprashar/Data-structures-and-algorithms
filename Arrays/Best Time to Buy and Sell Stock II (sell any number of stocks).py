class Solution:
    def maxProfit(self, prices):

        """
            - A stock can be bought once and told once, but we can do unlimited transactions.
            - Simply do as many profitable transactions as possible!

        """

        totalProfit = 0
        for i in range(1, len(prices)):

            if prices[i] > prices[i - 1]:
                totalProfit += prices[i] - prices[i - 1]

        return totalProfit
