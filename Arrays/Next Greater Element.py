"""
N = 4, arr[] = [1 3 2 4]
"""

def nextGreator(arr):
    stack = []
    ans = [-1] * len(arr)

    for i in range(len(arr)-1,-1,-1):

        while len(stack) > 0 and stack[-1] < arr[i]:
                stack.pop()

        if len(stack) == 0:
            ans[i] = -1 
            

        elif stack[-1] > arr[i]:
            ans[i] = stack[-1]

        stack.append(arr[i])

    return ans 

arr = [1,3,2,4]
print(nextGreator(arr))



        

