"""
WRITE ABOUT THE TIME COMPLEXITY HERE AND WHY IT IS BAD
"""
class Solution:
    def coinChangeHelper(self, n, coinList, currRes, res):

        if n == 0:
            res.append(sorted(currRes))
            return

        if n < 0:
            return

        for coin in coinList:
            currRes.append(coin)
            self.coinChangeHelper(n - coin, coinList, currRes, res)
            currRes.pop()

    def count(self, S, m, n):

        coinList = S
        currRes = []
        res = []
        self.coinChangeHelper(n, coinList, currRes, res)

        res = sorted(res)

        last = len(res) - 1

        if len(res) > 1:
            while last > -1:
                if res[last] == res[last - 1]:
                    res.pop(last)
                last -= 1

        return len(res)