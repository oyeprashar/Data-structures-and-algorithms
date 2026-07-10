from collections import deque

class Solution:
  
    def maxEqualSum(self, N1 ,N2 ,N3, s1, s2, s3):
        sum1 = sum(s1)
        sum2 = sum(s2)
        sum3 = sum(s3)
        dq1 = deque(s1)
        dq2 = deque(s2)
        dq3 = deque(s3)

        while len(dq1) > 0 and len(dq2) > 0 and len(dq3) > 0:

            if sum1 == sum2 == sum3:
                return sum1

            if sum1 >= sum2 and sum1 >= sum3:
                sum1 -= dq1[0]
                dq1.popleft()

            elif sum2 >= sum1 and sum2 >= sum3:
                sum2 -= dq2[0]
                dq2.popleft()

            else:
                sum3 -= dq3[0]
                dq3.popleft()

        return 0
