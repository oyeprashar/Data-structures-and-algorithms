"""
1XY2 is a valid shuffle of XY and 12
Y1X2 is a valid shuffle of XY and 12     
Y21XX is not a valid shuffle of XY and 12
"""

def isValidShuffle(str1,str2,shuffle):

    dict1 = {}

    for char in str1:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
        
    for char in str2:
        if char not in dict1:
            dict1[char] = 1
        else:
            dict1[char] += 1
        
    dict2 = {}

    for char in shuffle:
        if char not in dict2:
            dict2[char] = 1
        else:
            dict2[char] += 1
        
    if len(dict1) != len(dict2):
        return False 
    
    for char in dict2:

        if char not in dict1:
            return False 
        
        if dict2[char] != dict1[char]:
            return False 
    
    return True 

shuffle = "1XY2"
str1 = "XY"
str2 = "12"
print(shuffle,"is shuffle of",str1,"and",str2,":",isValidShuffle(str1,str2,shuffle))

shuffle = "Y1X2"
str1 = "XY"
str2 = "12"
print(shuffle,"is shuffle of",str1,"and",str2,":",isValidShuffle(str1,str2,shuffle))

shuffle = "Y21XX"
str1 = "XY"
str2 = "12"
print(shuffle,"is shuffle of",str1,"and",str2,":",isValidShuffle(str1,str2,shuffle))