"""
swap two chars in a string such that we get lexicographically smaller string
input = "abcabcpop"
output = "abcabcopo"
"""

class Solution:
    def LexicographicallyMinimum(self, str):
        temp = sorted(str)
        ch1 = '$'
        ch2 = '$'
        flag = False

        for i in range(len(str)):
            # print("============")
            k = str.index(temp[i])
            # print("i =",i,"temp[i] =",temp[i],"k =",k)

            for j in range(k):
                if str[j] > temp[i]:
                    # print(str[j],"is greator than",temp[i])
                    ch1 = str[j]
                    ch2 = temp[i]
                    flag = True
                    break

            if flag == True:
                break

        res = ""
        for char in str:
            if char == ch1:
                res += ch2
            elif char == ch2:
                res += ch1
            else:
                res += char

        return res
