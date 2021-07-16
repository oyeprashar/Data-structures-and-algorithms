"""
Remove Invalid Parentheses
Example 1:

Input: s = "()())()"
Output: ["(())()","()()()"]

Algo:
-> We need find out the number of brackets which are wrong, call it k
-> this is the minmium number of brackets we can remove to make the string balanced
-> now we can remove k brackets to make it balance
A string is balanced when minRemovals to make it balance == 0
"""

def minRemoval(str1):
    stack = []

    for bracket in str1:
        if bracket == '(':
            stack.append(bracket)

        elif bracket == ')':
            if len(stack) == 0:
                stack.append(bracket)
            elif stack[-1] == ')':
                stack.append(bracket)
            elif stack[-1] == '(':
                stack.pop()
    return len(stack)

def generate(str1,ans,k):

    if k == 0 and minRemoval(str1) == 0:
        ans.add(str1)
        return

    for i in range(len(str1)):
        newStr = str1[:i] + str1[i+1:]
        generate(newStr,ans,k-1)

def getBrackets(str1):
    k = minRemoval(str1)
    ans = set()
    generate(str1,ans,k)
    return ans

str1 = "()())()"
print(getBrackets(str1))

