"""
Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
"""

def findIndices(str1,str2):

    start = 0
    end = 0
    i = 0
    ans = []

    while end < len(str1):

        if str1[end] == str2[i]:

            if i == len(str2)-1:
                ans.append(start)
                i = 0 
                end = start + 1 
                start = end

            else:
        
                end += 1
                i += 1
            
        else:
            end = start + 1
            start = end 
            i = 0
        
    return ans 

str1 = "THIS IS A TEST TEXT"
str2 = "TEST"

print(findIndices(str1,str2))

str1 = "AABAACAADAABAABA"
str2 = "AABA"

print(findIndices(str1,str2))