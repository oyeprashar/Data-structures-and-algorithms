class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
		
class Solution:

    def multiple(self,head,num):

    	left = 0
    	curr = head 
    	last = None
    
    	while curr != None:
    
    		x = (curr.data * num) + left 
    	
    		if x > 9:
    			curr.data = x % 10
    			left = x // 10 
    		
    		else:
    			curr.data = x
    			left = 0
    		

    		last = curr
    		curr = curr.next
    	
    	if left > 0:
    	    exp = 1

    	    while left // exp > 0:
    	        lastDigit = int((left/exp)%10)
    	        last.next = Node(lastDigit)
    	        last = last.next
    	        exp *= 10


    def factorial(self, num):
        head = Node(1)

    	for x in range(1,num+1):
    		self.multiple(head,x)
    	
    	ans = ""
    	curr = head 
    
    	while curr != None:
    		ans += str(curr.data)
    		curr = curr.next 
    	
    	return ans[::-1]