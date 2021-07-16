"""
Input file:
3
0 99 3

2
49 50

8
16 17 15 0 20 1 1 2

10
0 0 100 0 0 0 0 0 0 0

4
6 0 0 10

-1

Output file:
34
-1
23
70
"""
while True:
    n = int(input())
    if n == -1:
        break
    list1 = list(map(int,input().split()))
    blank = input()
    
    if sum(list1) % len(list1) != 0:
        print(-1)
    else:
        perProcessor = sum(list1) / len(list1)
        ansMax = -3 ** 38

        for i in range(1,len(list1)+1):
            part1 = list1[:i]
            part2 = list1[i:]

            rn1 = sum(part1)
            req1 = len(part1) * perProcessor

            rn2 = sum(part2)
            req2 = len(part2) * perProcessor

            # print("part1 =",part1," rn =",rn1," req =",req1)
            # print("part2 =",part2," rn =",rn2," req =",req2)

            if rn1 < req1:
                diff1 = abs(rn1-req1)
                if diff1 > ansMax:
                    ansMax = diff1
                    # print("rn1 = ",rn1, " is less than req1 = ",req1," their abs diff is = ",diff1," ansMax =",ansMax)

            if rn2 < req2:
                diff2 = abs(rn2-req2)
                if diff2 > ansMax:
                    ansMax = diff2
                    # print("rn2 = ",rn2, " is less than req2 = ",req2," their abs diff is = ",diff2," ansMax =",ansMax)



        print(int(ansMax))