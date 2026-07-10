class Solution:

    def generateNumber(self, arr):
        p = 1
        num = 0

        for i in range(len(arr) - 1, -1, -1):
            num += (arr[i] * p)
            p *= 10

        return num

    # Genarate smallest number of d digits such that the sum of digits is s
    def smallestNumber(self, sumOfDigits, numberOfDigits):

        # impossible case!
        if sumOfDigits > 9 * numberOfDigits:
            return -1

        # To minimise the number, we will save "1" for the left most digit
        sumOfDigits -= 1
        number = [0] * numberOfDigits

        # run the loop from last index till 1st index
        for i in range(len(number)-1, 0, -1):

            if sumOfDigits >= 9:
                number[i] = 9
                sumOfDigits -= 9

            else:
                number[i] = sumOfDigits
                sumOfDigits = 0

        # putting the saved 1 and remaining number at the left most bit
        number[0] = 1 + sumOfDigits
        return self.generateNumber(number)

s = Solution()
print(s.smallestNumber(20, 3))
