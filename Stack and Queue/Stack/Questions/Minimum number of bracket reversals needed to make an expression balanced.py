import math

def countMinReversals(s):


    # step 1 : Find out the total number of brackets causing the string to be imbalanced

    stack = []

    for bracket in s:
        if bracket ==  "{":
            stack.append(bracket)

        elif bracket == "}":

            if len(stack) > 0 and stack[-1] == "{":
                stack.pop()

            else:
                stack.append(bracket)

    # this will contain all the brackets that are causing the string to imblanced
    # print(stack)

    # already balanced
    if len(stack) == 0:
        return 0

    if len(stack) % 2 == 1:
        return -1

    numberOfOpeningBrackets = stack.count('{')
    numberOfClosingBrackets = stack.count('}')

    """
    Intuition : 
        The main point to remember is that we are reversing brackets so for {{ we need to reverse just one of them 
        so number of unbalanced opening divided by 2. Same for the closing brackets.
    """

    return math.ceil(numberOfOpeningBrackets / 2) + math.ceil(numberOfClosingBrackets / 2)

print(countMinReversals("{{}{{{}{{}}{{"))
