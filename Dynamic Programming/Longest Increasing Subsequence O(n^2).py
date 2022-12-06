def LIS(arr):
    memory = [1] * len(arr)

    for i in range(1,len(arr)):

        ans = memory[i]
        
        for j in range(i):
            if arr[i] > arr[j]:
                curr = memory[j] + 1
                ans = max(ans,curr)

        memory[i] = ans

    return max(memory)

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(arr))