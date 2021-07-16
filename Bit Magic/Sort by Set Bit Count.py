"""
arr= [5, 2, 3, 9, 4, 6, 7, 15]
Output:
15 7 5 3 9 6 2 4 

Input: 
arr[] = {1, 2, 3, 4, 5, 6};
Output: 
3 5 6 1 2 4

Note: For integers having same number of set bits in their binary representation, 
      sort according to their position in the original array i.e., a stable sort
"""

# THIS CAN BE DONE IN ONE LINE ALSO IN O(1) SPACE COMPLEXITY BY USING LAMBDA FUNCTION
#  arr.sort(key=lambda x:bin(x).count("1"),reverse=True) <-------- IMPORTANT


class Item:
    def __init__(self,num,index):
        self.num = num
        self.index = index
        self.bits = self.countSetBits(num)

    def __lt__(self,otherObject):
        if self.bits == otherObject.bits:
            return self.index > otherObject.index

        else:
            return self.bits < otherObject.bits

    def countSetBits(self,num):
        res = 0
        while num > 0:
            res += 1
            num = num & (num-1)

        return res


class Solution:
    def sortBySetBitCount(self, arr, n):
        objArr = []
        for i in range(len(arr)):
            num = arr[i]
            index = i
            obj = Item(num,index)
            objArr.append(obj)
    
        objArr.sort(reverse=True)
        for j in range(len(objArr)):
            objArr[j] = objArr[j].num
            
        return objArr
s = Solution()
arr = [3, 1, 5]

print(s.sortBySetBitCount(arr,len(arr)))