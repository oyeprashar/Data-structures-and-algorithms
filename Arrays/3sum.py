class Solution:
    def hasTripletSum(self, arr, target):
        for i in range(len(arr) - 2):
            j = i + 1
            k = len(arr) - 1


            while j < k:

                if arr[i] + arr[j] + arr[k] == target:
                    return [i, j, k]

                elif arr[i] + arr[j] + arr[k] < target:
                    j += 1

                else:
                    k -= 1


            return None
