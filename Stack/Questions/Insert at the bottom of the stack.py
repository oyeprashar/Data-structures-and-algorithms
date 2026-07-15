"""
Insert at the bottom of the stack
"""

def insertBottom(stack,newData):

    if len(stack) == 0:
        stack.append(newData)
        return
    
    currData = stack.pop()
    insertBottom(stack,newData)
    stack.append(currData)
    
    

stack = [4,3,2,1]
newData = 5

insertBottom(stack,newData)

print(stack)