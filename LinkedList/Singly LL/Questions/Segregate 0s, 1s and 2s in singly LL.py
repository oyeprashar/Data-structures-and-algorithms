"""
❌ Since this is a singly linkedlist and we cannot move backwards, we cannot use dutch flag algo

✅ We maintain a array of constant size 3 and count the occurences and change the data of LL accordingly 
"""

class Solution:
    
    def segregate(self, head):
        count = [0] * 3
        
        curr = head 
        while curr != None:
            count[curr.data] += 1
            curr = curr.next
        
        curr = head
        for i in range(len(count)):
            
            currCount = count[i]
            num = i
            
            while currCount != 0 and curr != None:
                currCount -= 1
                curr.data = num
                curr = curr.next
            
        return head