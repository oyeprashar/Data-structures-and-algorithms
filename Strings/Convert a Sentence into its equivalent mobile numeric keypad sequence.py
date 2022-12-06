def convert(str1):

    keyPad = [2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999]
    ans = ""

    for char in str1:
        if char == " ":
            ans += '0'
        else:
            index = ord(char) - ord('A')
            ans += str(keyPad[index])
    
    return ans 

str1 = "GEEKSFORGEEKS"

print(convert(str1))