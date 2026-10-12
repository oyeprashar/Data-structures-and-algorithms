"""
Merging intervals

cases :
    1. first interval -- just pick it
    2 non overlapping with last -- just take it
    3. Overlapping - remove the last interval -- insert merged interval
"""

class Solution:
    def merge(self, intervals):

        # we sort by the starting so that we can merge overlapping
        intervals.sort()
        stack = []


        for currStart, currEnd in intervals:


            # case 1 & case 2 : either the stack is empty or no overlap is there
            if len(stack) == 0 or currStart > stack[-1][1]:
                stack.append([currStart, currEnd])

            # case 3 : overlapping intervals
            else:
                stackTopStart, stackTopEnd = stack[-1]

                newInterval = [stackTopStart, max(currEnd, stackTopEnd)]
                stack.pop()
                stack.append(newInterval)

        return stack
