"""
We use max heap because we want to arrange the high frequency characters around the low frequency ones so that the
adjacent characters are not duplicate
"""
import heapq


class Item:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

    def __lt__(self, other):
        return self.freq >= other.freq


class Solution:

    def canRearrange(self, s):

        freqDict = {}

        for char in s:
            if char not in freqDict:
                freqDict[char] = 1
            else:
                freqDict[char] += 1

        maxHeap = []
        for key in freqDict:
            heapq.heappush(maxHeap, Item(key, freqDict[key]))

        res = ""

        while len(maxHeap) >= 2:

            top1 = heapq.heappop(maxHeap)
            top2 = heapq.heappop(maxHeap)

            res += top1.char
            res += top2.char

            if top1.freq - 1 > 0:
                top1.freq -= 1
                heapq.heappush(maxHeap, top1)

            if top2.freq - 1 > 0:
                top1.freq -= 1
                heapq.heappush(maxHeap, top2)

        if len(maxHeap) == 1:
            if maxHeap[-1].freq > 1:
                return False
            else:
                res += maxHeap[-1].char

        return True
