def merge(ranges):
    stack = []
    stack.append(ranges[0])

    for i in range(1,len(ranges)):
        if ranges[i][0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1],ranges[i][1])
        else:
            stack.append(ranges[i])
    return stack

def kthNumber(ranges,k):
    for list1 in ranges:
        print("curr k =",k)
        if (list1[1] - list1[0]) + 1 >= k: # if k lies within the current range, we can find it easily
            return (list1[0] + k) - 1
        else:
            k -= ((list1[1] - list1[0]) + 1) # if it doesnt not lie in the current range we just subtract the current range from k
    return -1


def getKthNumber(ranges,k):
    ranges.sort()
    ranges = merge(ranges)
    return kthNumber(ranges,k)

ranges = [[2,4],[5,8]]
k = 7
print(getKthNumber(ranges,k))

