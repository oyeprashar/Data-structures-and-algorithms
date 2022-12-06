class Solution:
    def countNum(self,left,right,rowIndex,matrix,key,ans):

        if left <= right:
    
            mid = (left+right) // 2
    
            if matrix[rowIndex][mid] <= key:
                ans[0] = mid+1
                return self.countNum(mid+1,right,rowIndex,matrix,key,ans)
            
            else:
                return self.countNum(left,mid-1,rowIndex,matrix,key,ans)
                
                
    def findMedian(self,left,right,mat,reqCount):

        if left <= right:
    
            mid = (left+right) // 2
    
            totalCount = 0
            
    
            for row in range(len(mat)):
                cnt = [0]
                self.countNum(0,len(mat[row])-1,row,mat,mid,cnt)
                totalCount += cnt[0]
    
            if totalCount < reqCount:
                return self.findMedian(mid+1,right,mat,reqCount)
            
            else:
                return self.findMedian(left,mid-1,mat,reqCount)

        else:
            return left

    def median(self, matrix, r, c):
    	left = 0
        right = 10**9
        totalCount = 0
        
        for row in range(len(matrix)):
            totalCount += len(matrix[row])
        
        reqCount = (totalCount//2) + 1
        
        return self.findMedian(left,right,matrix,reqCount)


        