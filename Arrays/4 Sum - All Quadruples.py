
"""
How to avoid duplicates?
    - The problem statements want us to not return duplicate quadruplet (by value and not index)
    - so 1 2 1 2 is same as 2 1 2 1
    - So make the above to cases 1 1 2 2 we sort the array and then use a set to eliminate the duplicates
"""




class Solution:
    def fourSum(self, arr, target):

        arr.sort()
        res = set()

        for i in range(len(arr) - 3):
            for j in range(i + 1, len(arr) - 2):

                left = j + 1
                right = len(arr) - 1

                while left < right:

                    currSum = arr[i] + arr[j] + arr[left] + arr[right]

                    if currSum == target:
                        res.add((arr[i], arr[j], arr[left], arr[right]))
                        left += 1
                        right -= 1

                    elif currSum < target:
                        left += 1

                    else:
                        right -= 1

        ans = []
        for element in res:
            ans.append(list(element))

        return sorted(ans)

