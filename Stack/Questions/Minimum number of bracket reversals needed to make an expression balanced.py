import math

def countRev(s):
    
    stack = []
    
    for bracket in s:
        
        if bracket == "{":
            stack.append(bracket)
        
        elif bracket == "}":
            
            if len(stack) == 0 or stack[-1] != "{":
                stack.append(bracket)
            
            elif stack[-1] == "{":
                stack.pop()
            
                
    if len(stack) == 0:
        return 0
    
    if len(stack) % 2 == 1:
        return -1
            
    opening = stack.count("{")
    closing = len(stack) - opening
    
    ans = math.ceil(opening/2) + math.ceil(closing/2)
    
    return ans
