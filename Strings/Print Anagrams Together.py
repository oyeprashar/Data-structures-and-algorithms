from collections import defaultdict

class Solution:
    def Anagrams(self, words, n):
        
        dict1 = defaultdict(list)
        
        for word in words: # O(n)
            
            # O(m + mlogm) = O(mlogm)
            key = "".join(sorted(word))
            dict1[key].append(word)
            
        # total time = O(n*mlogm)
        
        
        ans = []
        for key in dict1:
            currList = dict1[key]
            
            ans.append(currList)
        
        return ans
