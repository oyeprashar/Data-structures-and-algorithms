
def reverse(stack):
    if len(stack) == 0:
        return None 
    
    currPop = stack.pop(0)
    reverse(stack)
    print(currPop)

stack = [1,2,3,4]
reverse(stack)
    
