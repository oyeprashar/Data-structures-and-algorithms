def betterOrder(arr):
    ans = []

    oneCount = arr.count(1)

    for x in range(oneCount):
        ans.append(1)
    
    arr.sort(reverse = True)

    if len(arr) - oneCount == 2:
        if arr[0] == 3 and arr[1] == 2:
            ans.append(2)
            ans.append(3)
        
            return " ".join(str(num) for num in ans)
    
    for num in arr:
        if num != 1:
            ans.append(num)
    return " ".join(str(num) for num in ans)


test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    arr = [int(num) for num in input().split()]
    print(betterOrder(arr))


