

class Solution:
    
    
    def isValid(self,currMax,pages,noOfStudents):
        reqStudents = 1
        pagesRead = 0
    
        for page in pages:
            
            if page > currMax: # this currMax is smaller than number of pages in one of the book, it means maanlo agar koi sirf yeh kitbaad bhi padhta hai toh
                return False   # usske more than currMax padhna padega which means yeh currMax valid/possible nhi hai3
    
            pagesRead += page
    
    
            if pagesRead > currMax:
                reqStudents += 1
                pagesRead = page
    
    
         `  if reqStudents > noOfStudents:
                return False
    
        if reqStudents > noOfStudents:
            return False
        return True

    def minimizePages(self,left,right,noOfStudents,pages,ans):
    
        if left <= right:
    
            mid = (left+right) // 2
    
            if self.isValid(mid,pages,noOfStudents) is True:
                # save and move to left to minmize it
                ans[0] = mid
                return self.minimizePages(left,mid-1,noOfStudents,pages,ans)
            else:
                # else move to right and find a valid ans
                return self.minimizePages(mid+1,right,noOfStudents,pages,ans)
    


    def findPages(self,pages, n, noOfStudents):SS
        
        left = 0
        right = sum(pages)
        ans = [-1]
        self.minimizePages(left,right,noOfStudents,pages,ans)
        return ans[0]