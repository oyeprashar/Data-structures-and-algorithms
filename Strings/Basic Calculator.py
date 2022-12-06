"""
"(1+(4+5+2)-3)+(6+8)"
"""

def basicCalculator(str1):

    currSum  = 0
    lastSymbol = None
    stack = []

    for i in range(len(str1)):

        if str1[i] == '(':
            stack.append(currSum)
            currSum = 0
            stack.append(lastSymbol)
            lastSymbol = None 
        
        elif str1[i] == ')':
            sym = stack.pop()
            if sym == '-':
                currSum *= -1 
            
            prevSum = stack.pop()

            currSum += prevSum

        elif str1[i] == '+' or str1[i] == '-':
            
            if i - 1 >= 0 and str1[i-1] == '+' or str1[i-1] == '-':

                prev = str1[i-1]
                curr = str1[i]

                if (prev == '+' and curr == '+') or (prev == "-" and curr == '-'):
                    lastSymbol = '+'
                
                elif (prev == '+' and curr == '-') or (prev == "-" and curr == '+'):
                    lastSymbol = '-'
                
            else:
                lastSymbol = str1[i]
        
        else:
            if lastSymbol == '+' or lastSymbol == None:
                currSum += (ord(str1[i]) - ord('0'))
            
            elif lastSymbol == '-':
                currSum -= (ord(str1[i]) - ord('0'))
            
    return currSum


str1 = "(1+(4+5+2)-3)+(6+8)"
print(basicCalculator(str1))