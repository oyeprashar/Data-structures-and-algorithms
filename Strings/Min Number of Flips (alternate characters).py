"""
The question is simpler than it may appear. There can always be two cases. Let's take an example of a string of size 3.
It can either be 101 or 010. For both the cases we count the number of flips needed and return the min of case1 and case2
"""



class Solution:
    def minFlips(self, s):

        case1 = 0
        case2 = 0
        flag = 0

        for char in s:

            # at even postions in case one we want 1 and case2 0
            if flag % 2 == 0:

                if char == "1":
                    case2 += 1

                else:
                    case1 += 1

            # at odd postions case1 wants
            else:

                if char == "1":
                    case1 += 1

                else:
                    case2 += 1

            flag += 1

        return min(case1, case2)
