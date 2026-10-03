"""
Find smallest d digit number with sum s
"""


class Solution:

    def smallestNumber(self, sumOfDigits, numberOfDigits):

        # if its impossible to get the sum even with all 9s
        if sumOfDigits > numberOfDigits * 9:
            return -1

        # we want to use the 1 on the left most place to minimise the num
        sumOfDigits -= 1
        number = ["0"] * numberOfDigits

        # the loop won't go to the index 0s
        for i in range(len(number) - 1, 0, -1):

            if sumOfDigits >= 9:
                number[i] = str(9)
                sumOfDigits -= 9

            else:
                number[i] = str(sumOfDigits)
                sumOfDigits = 0
                break

        # place 1 on the left most place (and add whatever was left)
        number[0] = str(1 + sumOfDigits)
        return "".join(number)

