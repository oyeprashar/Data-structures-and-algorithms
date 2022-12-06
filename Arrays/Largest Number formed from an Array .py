class Item:
    def __init__(self,num):
        self.num = num
    
    def __lt__(self,otherObj):
        xy = str(self.num) + str(otherObj.num)
        yx = str(otherObj.num) + str(self.num)
        
        if xy > yx:
            return True
        else:
            False
            
class Solution:

    def printLargest(self,arr):
    
        objList = []
        
        for num in arr:
            currItem = Item(num)
            objList.append(currItem)
        
        objList.sort()
        
        ans = ""
        
        for item in objList:
            ans += str(item.num)
        
        return ans
        