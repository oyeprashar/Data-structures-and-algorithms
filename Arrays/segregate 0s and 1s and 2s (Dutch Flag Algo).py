"""
[ 0s ][ 1s ][ unknown ][ 2s ]
        ↑       ↑         ↑
       low     mid       high


[0, low - 1] -> all 0s
[low to mid - 1] -> all 1s
[mid ... high] → We don't know what they are, and we process them
[high + 1, end] -> all 2s
"""

class Solution:
    def sort012(self, arr):
        low = 0  # for 0
        mid = 0  # for 1
        high = len(arr) - 1 # for 2


        while mid <= high:

            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1

            elif arr[mid] == 1:
                mid += 1


            # Here when we are swapping mid with high, we are not sure what new element is sitting at mid
            # So we just move the high pointer and keep the mid where it was to process the new element
            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr
