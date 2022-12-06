def merge(ranges):
    ranges.sort()
    stack = []
    stack.append(ranges[0])

    for i in range(1,len(ranges)):
        if ranges[i][0] <= stack[-1][1]:
            stack[-1][1] = max(stack[-1][1],ranges[i][1])
        else:
            stack.append(ranges[i])
    return stack

ranges = [[2,13],[8,20]]
print(merge(ranges))