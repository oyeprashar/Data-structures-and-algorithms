INT_MIN = -3**38
INT_MAX = 3**38
class Solution:


    def binarySearch(self,left,right,arr1,arr2):

        if left <= right:

            mid = (left+right) // 2

            cut1 = mid 
            cut2 = ((len(arr1)+len(arr2)+1) // 2) - cut1

            l1 = INT_MIN
            r1 = INT_MAX 
            l2 = INT_MIN 
            r2 = INT_MAX 

            if cut1 - 1 >= 0:
                l1 = arr1[cut1-1]

            if cut1 < len(arr1):
                r1 = arr1[cut1]

            if cut2-1 >= 0:
                l2 = arr2[cut2-1]

            if cut2 < len(arr2):
                r2 = arr2[cut2]


            if l1 <= r2 and l2 <= r1:


                if (len(arr1)+len(arr2)) % 2 == 0:
                    return (max(l1,l2)+min(r1,r2)) / 2

                else:
                    return max(l1,l2)

            elif l1 > r2:
                return self.binarySearch(left,mid-1,arr1,arr2)

            else:
                return self.binarySearch(mid+1,right,arr1,arr2)
        
        return 0.0
            
    def findMedianSortedArrays(self, nums1, nums2):
        
        if len(nums1) < len(nums2):
            return self.binarySearch(0,len(nums1),nums1,nums2)
        
        else:
            return self.binarySearch(0,len(nums2),nums2,nums1)




            