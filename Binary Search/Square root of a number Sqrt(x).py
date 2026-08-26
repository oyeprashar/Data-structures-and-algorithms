class Solution:


    def binarySearch(self, left, right, num, ans):

        if left > right:
            return

        mid = (left + right) // 2

        if mid * mid <= num:
            ans[0] = mid
            return self.binarySearch(mid + 1, right, num, ans)

        else:
            return self.binarySearch(left, mid -1, num, ans)


    # overall TC : O(logn)
    def sqrt(self, num):
        """
        Find n s.t. n*n <= num
        """
        ans =[-1]
        self.binarySearch(0, num * num, num, ans)
        result = ans[0]

        increment = 0.1
        precision = 2

        """
        The integer is already the greatest possible and we cannot make 3.0 to 4.0
        Because of this each precision place runs 9 times and cannot run more than that to change the int
        """

        # O(9 (times each increment runs) * 2 (precision place)
        for _ in range(precision):

            while (result + increment) ** 2 <= num:
                result += increment

            increment /= 10 # keep increasing the decimal places

        # Round to remove floating-point artifacts because decimals like 0.1 and 0.01
        # cannot always be represented exactly in binary (e.g. 3.1600000000000006 -> 3.16)
        return round(result, 2)

s = Solution()
print(s.sqrt(51))
