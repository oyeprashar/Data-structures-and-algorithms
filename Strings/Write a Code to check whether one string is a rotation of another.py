"""
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
"""

def isRotation(str1,str2):

    string = str1+str1 

    i = 0
    j = 0

    while i < len(string):

        if j == len(str2):
            return True 
        
        if string[i] == str2[j]:
            i += 1
            j += 1
        
        else:
            j = 0
            i += 1

    return False 


str1 = "ABCD"
str2 = "CDAB"

print(str2,"is rotation of",str1,":",isRotation(str1,str2))

str1 = "ABCD"
str2 = "ACBD"

print(str2,"is rotation of",str1,":",isRotation(str1,str2))