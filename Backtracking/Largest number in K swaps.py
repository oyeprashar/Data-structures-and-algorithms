#User function Template for python3

class Solution:

    def generate(self,currIndex,k,arr,max1):

        num = int("".join(arr))
        max1[0] = max(max1[0],num)

        if currIndex == len(arr) or k == 0:
            return 

        maxElement = int(arr[currIndex])
        for j in range(currIndex+1,len(arr)):
                maxElement = max(maxElement,int(arr[j]))

        # if maxElement is same as the currIndex, i means currIndex waaala element it means currIndex waala element is at its correct position and
        # usske right me usske bada element nhi hai so we move on to next index

        if maxElement == int(arr[currIndex]):
            self.generate(currIndex+1,k,arr,max1) 

        # we need to swap the currIndex element with all the occurences of the maxElement! taki saare possible combinations generate ho jaye
        for i in range(currIndex+1,len(arr)):
            if int(arr[i]) == maxElement:

                arr[i],arr[currIndex] = arr[currIndex],arr[i]
                self.generate(currIndex+1,k-1,arr,max1)
                arr[i],arr[currIndex] = arr[currIndex],arr[i]
    
    def findMaximumNum(self,s,k):
        currIndex = 0
        arr = [char for char in s]
        max1 = [-3**38]
        self.generate(currIndex,k,arr,max1)
        return max1[0]




k = 3
string = "4551711527"
s = Solution()
print(s.findMaximumNum(string,k))