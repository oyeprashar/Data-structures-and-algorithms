"""
Approach  :
    - We want to pick the highest profit job first
    - So we sort the list by the profit in decreasing order
    - Then we schedule them as late as possible


Why do we want to schedule a job as late as possible?
    This is because the earlier slots can cater to alot of jobs while the later jobs can cater to lesser jobs.
    For example a slot 2 can cater to job with deadline 2 or more so jobs with deadline [2, 3, 4, 5] but slot 5 can only
    cater to job with deadline 5


"""


class Solution:
    def jobSequencing(self, deadline, profit):

        jobs = []

        for i in range(len(deadline)):
            jobs.append([profit[i], deadline[i]])

        jobs.sort(reverse=True, key=lambda x: x[0])

        jobsExecuted = 0
        totalProfit = 0
        schedule = [False] * len(deadline) # False means the slow is empty

        for job in jobs:

            currIndex = job[1] - 1

            while currIndex >= 0 and schedule[currIndex] != False:
                currIndex -= 1

            if currIndex >= 0:
                schedule[currIndex] = True
                jobsExecuted += 1
                totalProfit += job[0]


        return [jobsExecuted, totalProfit]
