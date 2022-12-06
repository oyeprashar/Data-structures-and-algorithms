class Solution:

    """
    For both the time complexity is O(N) | Space complexity is O(1)
    """
    def atoi(self,string):
        
        ans = 0
        place = 1
        i = len(string)-1
        
        while i >= 0:
            if i == 0 and string[0] == "-":
                ans *= -1
                break
            
            if ord(string[i]) - ord("0") < 0 or ord(string[i]) - ord("0") > 9:
                return -1
            
            num = ord(string[i]) - ord("0")
            ans += num * place
            
            i -= 1
            place *= 10
        
        return ans
        
    def atoi(self,string):

        # THIS WILL WORK IN PYTHON 
        dict1 = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        place = 1
        
        ans = 0
        i = len(string)-1
        
        while i >= 0:
            
            if i == 0 and string[i] == "-":
                ans = ans*-1
                break
            
            if string[i] not in dict1:
                return -1
            
            num = dict1[string[i]]
            ans += num*place
            
            i -= 1
            place *= 10
        
        return ans

        
      