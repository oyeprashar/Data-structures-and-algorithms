def precendance(currOp):
    if currOp == '+' or currOp == '+':
        return 1 
    
    if currOp == '*' or currOp == '/':
        return 2
    

def operate(num1,num2,op):
    if op == '+':
        return num1 + num2 

    elif op == '-':
        return num1 - num2
        
    elif op == '*':
        return num1 * num2
    
    if op == '/':
        return num1 / num2


def evaluate(str1):

    operatorStack = []
    operandStack = []

    for char in str1:

        if char == '(':
            operatorStack.append(char)
        
        elif ord(char) - ord('0') >= 0 and ord(char) - ord('0') <= 9:
            operandStack.append(ord(char) - ord('0'))
            
        elif char == ')':
            
            while operatorStack[-1] != '(':
                top2 = operandStack.pop()
                top1 = operandStack.pop()
                op = operatorStack.pop()
                newVal = operate(top1,top2,op)
                operandStack.append(newVal)

            operatorStack.pop()

        elif char == '+' or char == '-' or char == '*' or char == '/':
            while len(operatorStack) > 0 and operatorStack[-1] != '(' and precendance(char) <= precendance(operatorStack[-1]):
                top2 = operandStack.pop()
                top1 = operandStack.pop()
                op = operatorStack.pop()
                newVal = operate(top1,top2,op)
                operandStack.append(newVal)
            
            operatorStack.append(char)
        
    while len(operatorStack) > 0:
        top2 = operandStack.pop()
        top1 = operandStack.pop()
        op = operatorStack.pop()
        newVal = operate(top1,top2,op)
        operandStack.append(newVal)
    
    return operandStack[-1]

# the number would range from 0-9

str1 = "2+3*6"
print(evaluate(str1))




                



