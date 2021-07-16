"""
2 

7
noobz 1
llamas 2
Winn3rz 2
5thwheel 1
NotoricCoders 5
StrangeCase 7
WhoKnows 7

3
ThreeHeadedMonkey 1
MoscowSUx13 1
NeedForSuccess 1

Output:
5
3
"""

# TIME COMPLEXITY = O(N) 
# Counting sort ka algo use kro bhai kyo ki cummulative count gives positions (RANK)
test_case = int(input())
for _ in range(test_case):
    blankLine = input()
    n = int(input())
    list1 = []

    for i in range(n):
        name, wRank = input().split()
        list1.append(int(wRank))

    maxElement = max(list1)
    count = [0] * (maxElement + 1)

    for num in list1:
        count[num] += 1

    # convert the count into cummulative count array
    prev = count[0]
    for i in range(1,len(count)):
        count[i] += prev
        prev = count[i]

    ans = 0

    for num in list1:
        wantedRank = num
        currRank = count[num]
        count[num] -= 1
        diff = abs(wantedRank - currRank)
        ans += diff

    print(ans)





