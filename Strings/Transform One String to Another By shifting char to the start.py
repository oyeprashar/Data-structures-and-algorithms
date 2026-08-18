def minOperations(str1,str2):

    count = 0
    i = len(str1)-1
    j = len(str2)-1

    while i >= 0:

        if str1[i] == str2[j]:
            i -= 1
            j -= 1

        else:

            """
            We count from the end because it preserves the order the question wants. We move the ith pointer in the
            string1 and keep on counting the mismatches
            """
            while i >= 0 and str1[i] != str2[j]:
                i -= 1
                count += 1
    
    return count 

str1 = "EACBD"
str2 = "EABCD"

print(minOperations(str1,str2))

str1 = "ABD" 
str2 = "BAD"
print(minOperations(str1,str2))