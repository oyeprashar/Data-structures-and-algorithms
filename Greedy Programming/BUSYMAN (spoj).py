class Item:
        def __init__(self,startTime,finishTime):
            self.startTime = startTime
            self.finishTime = finishTime
            
        def __lt__(self,otherObject):
            return self.finishTime < otherObject.finishTime
            
class Solution:
    
            
    def maximumMeetings(self,n,start,end):
        
       
        objList = []
        
        for i in range(n):
            startTime = start[i]
            finishTime = end[i]
            currObject = Item(startTime,finishTime)
            objList.append(currObject)
            
        objList = sorted(objList)
        
        obj1 = objList[0]
        prevFinishTime = obj1.finishTime
        res = 1
        
        ans = []
        ans.append((obj1.startTime,obj1.finishTime))
        
       
        
        for i in range(1,len(objList)):
            curr = objList[i]
            
            if curr.startTime > prevFinishTime:
                
                res += 1
                prevFinishTime = curr.finishTime
              
        return res
