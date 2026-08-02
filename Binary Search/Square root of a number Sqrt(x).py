class Solution:

    def binarySearch(self, left, right, target, ans):

        # print("current state of ans :", ans)

        if left > right:
            return

        mid = (left + right) // 2

        # print("current state of mid :", mid)

        if mid * mid <= target:
            ans[0] = mid
            # move right to maximise it
            return self.binarySearch(mid + 1, right, target, ans)

        else:
            return self.binarySearch(left, mid - 1, target, ans)

    def mySqrt(self, x: int) -> int:

        """
        a number whose
        sqrtx = y

        y * y == x

        we do the binary search to find this y
        """

        ans = [None]
        self.binarySearch(0, x, x, ans)
        return ans[0]
