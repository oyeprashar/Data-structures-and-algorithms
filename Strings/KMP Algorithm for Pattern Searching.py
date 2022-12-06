def getArr(pat):
    x = 0 
    y = 1
    arr = [0] * len(pat)

    while y < len(pat):

        if pat[x] == pat[y]:
            arr[y] = 1 + x 
            x += 1
            y += 1
        
        elif pat[x] != pat[y]:

            if x == 0:
                arr[y] = 0
                y += 1
            
            else:

                x = arr[x-1]
            
    return arr 


def KMP(str1,pat):

    lps = getArr(pat)


    i = 0
    j = 0

    while i < len(str1):

        if str1[i] == pat[j]:
            i += 1
            j += 1
        
        if j == len(pat):
            print("pattern found at index =",i-j)
            j = lps[j-1]

        if j < len(pat) and str1[i] != pat[j]:

            if j != 0:
                j = lps[j-1]
            
            else:
                i += 1

txt = "ABABDABACDABABCABAB"
pat = "ABABCABAB"
KMP(txt,pat)
        
