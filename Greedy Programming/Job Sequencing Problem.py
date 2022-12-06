class Solution:
    
    def JobScheduling(self,Jobs,n):
        
        details = []
        
        for job in Jobs:
            details.append([job.profit,job.deadline])

        
        details.sort(reverse = True)
        
        count = 0
        totalProfit = 0
        
        schedule = [False] * n
        
        for item in details:
            
            currIndex = item[1] - 1
            
            currIndex = min(currIndex,n-1)
            while schedule[currIndex] != False and currIndex >= 0:
                
                currIndex -= 1
              
            
            if currIndex >= 0:# and schedule[currIndex] == 0:
                schedule[currIndex] = True
                count += 1
                totalProfit += item[0]
      
        return [count, totalProfit]
        