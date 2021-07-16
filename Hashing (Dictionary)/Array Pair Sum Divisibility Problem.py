class Solution:

    def canPair(self, nuns, k):
       # if nuns == [13,13]:
       #     return False
        if len(nuns) % 2 !=0:
            return False
        
        dict1 = {}
        
        for num in nuns:
           rem = num % k

           
           if rem in dict1:
               dict1[rem] += 1
           else:
               dict1[rem] = 1
        print(dict1)

        for rem in dict1:
           
           if rem * 2 == k:
               if dict1[rem] % 2 != 0:
                   return False
                   
           elif rem == 0:
               if dict1[rem] % 2 != 0:
                   return False
           else:
               
               otherRem = k - rem
               if otherRem in dict1:
                   if dict1[rem] != dict1[otherRem]:
                       return False
                       
               if otherRem not in dict1:
                   return False
           
        return True


k = 6
arr =[9, 5, 7, 3, 18, 21,36,60,66,72]
arr2 = [2, 4, 1, 3]

s = Solution()
print(s.canPair(arr,k))
print("=======================================")
print(s.canPair(arr2,4))