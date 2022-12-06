def isPossible(str1):

    count0 = 0 
    count1 = 0
    partion = 0

    i = 0
    while i < len(str1):
        if str1[i] == "0":
            count0 += 1
        
        elif str1[i] == "1":
            count1 += 1
        
        if count0 == count1:
            count1 = count0 = 0
            partion += 1
        
        i += 1
    
    if count0 == count1:
        return partion
    
    else:
        return -1 
    
str1 = "0100110101"
print(isPossible(str1))

str2 = "0111100010"
print(isPossible(str2))

str3 = "0000000000"
print(isPossible(str3))