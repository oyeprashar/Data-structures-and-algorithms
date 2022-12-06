class Solution:

    def minWindow(self, s: str, t: str) -> str:
        
        
        t_dict ={}
        for char in t:
            if char not in t_dict:
                t_dict[char] = 1
            else:
                t_dict[char] += 1
            
        reqCount = len(t_dict)
        
        s_dict = {}
        currCount = 0
        start = 0
        end = 0
        
        ans = [3**38,-1,-1]
        
        
        while True:
            
            if currCount < reqCount and end == len(s):
                break
            
            if currCount < reqCount:
                char = s[end]
                
                if char not in s_dict:
                    
                    s_dict[char] = 1
                else:
                    s_dict[char] += 1
            
                if char in t_dict and t_dict[char] == s_dict[char]:
                    currCount += 1
                    
                end += 1
                
            elif currCount == reqCount:
                
                currLen = ((end-1)-start)+1
                
                if currLen < ans[0]:
                    ans[0] = currLen
                    ans[1] = start
                    ans[2] = end
                
                char = s[start]
                
                s_dict[char] -= 1
                
                if char in t_dict and s_dict[char] < t_dict[char]:
                    currCount -= 1
                
                start += 1
            
        i = ans[1]
        j = ans[2]
        currStr = s[i:j]
        
        if i == -1 and j == -1:
            return ""
        
        return currStr
                