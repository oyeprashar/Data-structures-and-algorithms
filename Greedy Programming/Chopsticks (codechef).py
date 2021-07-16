n,d = map(int,input().split())
stickList = []
for _ in range(n):
    item = int(input())
    stickList.append(item)

stickList = sorted(stickList)
res = 0
i = 0

while i < len(stickList) - 1:
    if i + 1 > len(stickList)-1:
        break

    if stickList[i+1] - stickList[i] <= d:
        res += 1
        i += 2
    else:
        i += 1

print(res)