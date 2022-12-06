"""
Link: https://leetcode.com/problems/reorganize-string/
Time complexity = O(NlogN)
"""
import heapq


class Item:
    def __init__(self, char, count):
        self.char = char
        self.count = count

    def __lt__(self, otherObject):
        return self.count > otherObject.count


class Solution:
    def reorganizeString(self, s: str) -> str:

        dict1 = {}
        for char in s:
            if char not in dict1:
                dict1[char] = 1
            else:
                dict1[char] += 1

        max_heap = []

        for char in dict1:
            count = dict1[char]
            obj = Item(char, count)
            heapq.heappush(max_heap, obj)

        ans = ""

        while len(max_heap) > 1:  # agar len of heap == 0 we cannot pop two element and this will throw an erroR
            print(len(max_heap))
            top1 = heapq.heappop(max_heap)
            top2 = heapq.heappop(max_heap)

            ans += top1.char
            ans += top2.char

            if top1.count - 1 > 0:
                top1.count -= 1
                heapq.heappush(max_heap, top1)

            if top2.count - 1 > 0:
                top2.count -= 1
                heapq.heappush(max_heap, top2)

        if len(max_heap) == 1:
            if max_heap[0].count > 1:  # matlab repeat huye ga its not possible ki adjacent se alag ho
                return ""
            else:
                ans += max_heap[0].char
        return ans
