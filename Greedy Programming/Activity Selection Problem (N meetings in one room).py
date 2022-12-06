class Solution:
    
    def maximumMeetings(self,n,start,end):
        
        meetings = []
        
        for i in range(len(start)):
            meetings.append([start[i],end[i]])
        
        meetings.sort(key = lambda item : item[1])
    
        canDoMeetings = 1
        lastFinishTime = meetings[0][1]
        
        for i in range(1,len(meetings)):
            
            if meetings[i][0] > lastFinishTime:
                canDoMeetings += 1
                lastFinishTime = meetings[i][1]
            
        
        return canDoMeetings