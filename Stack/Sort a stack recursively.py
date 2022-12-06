"""
Recursively sort a stack
"""
def sortStack(stack):
    
    if len(stack) == 0:
        return 
    
    currData = stack.pop()
    sortStack(stack) 
    
    if len(stack) == 0:
        stack.append(currData)
    
    else:

        if currData > stack[-1]:
            stack.append(currData)
        
        else:
            poppedStack = []
            while len(stack) > 0 and currData < stack[-1]:
                poppedStack.append(stack.pop())
            
            stack.append(currData)

            while len(poppedStack) > 0:
                stack.append(poppedStack.pop())

stack = [11,2,32,3,41]

sortStack(stack)

print(stack)

