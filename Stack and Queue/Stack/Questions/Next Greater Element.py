class Solution:
    def nextLargerElement(self,arr,n):
        
        ans = [-1]
        stack = [arr[-1]]
        
        index = len(arr) - 2
        
        while index >= 0:
            
            if stack[-1] > arr[index]:
                ans.append(stack[-1])
                stack.append(arr[index])
            
            else:
                while len(stack) != 0 and stack[-1] <= arr[index]:
                    stack.pop()
                
                if len(stack) == 0:
                    ans.append(-1)
                    stack.append(arr[index])
                
                else:
                    ans.append(stack[-1])
                    stack.append(arr[index])
            
            index -= 1
        
        return ans[::-1]