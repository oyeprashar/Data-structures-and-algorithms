class Solution:
    def sort012(self, arr):
        low = 0  # for 0
        mid = 0  # for 1
        high = len(arr) - 1 # for 2


        while mid <= high:

            """
            This is the most important part. Since low and mid were initialised with the same index,
            elements till low - 1 are all zeroes
            """
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low += 1

            elif arr[mid] == 1:
                mid += 1


            elif arr[mid] == 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr

