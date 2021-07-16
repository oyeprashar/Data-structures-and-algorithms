def maxProfix(arr1,arr2):

    i = 0
    j = 0
    sum1 = sum2 = ans = 0

    while i < len(arr1) and j < len(arr2):

        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1

        elif arr2[j] < arr1[i]:
            sum2 += arr2[j]
            j += 1

        if i < len(arr1) and j < len(arr2):
            if arr1[i] == arr2[j]:
                sum1 += arr1[i]
                sum2 += arr2[j]
                ans += max(sum1,sum2)
                i += 1
                j += 1
                sum1 = sum2 = 0


    while i < len(arr1):
        sum1 += arr1[i]
        i += 1

    while j < len(arr2):
        sum2 += arr2[j]
        j += 1

    ans += max(sum1,sum2)
    return ans


arr11 = [-5,100,1000,1005]
arr21 = [-12,1000,1001]
arr12 = [3, 5, 7, 9, 20, 25, 30, 40, 55, 56, 57, 60, 62]
arr22 = [1, 4, 7, 11, 14, 25, 44, 47, 55, 57, 100]

print(maxProfix(arr11,arr21))
print(maxProfix(arr12,arr22))