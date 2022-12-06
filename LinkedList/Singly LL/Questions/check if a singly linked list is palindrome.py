"""
===== Approachs =====
Naive approach: In this approach we just traverse the LinkedList and store the concatenate the data of each node in a str1
                return str1 == str1[::-1] 
                Time complexity = O(n)
                Space complexity = O(n)

Efficient approach:
                If we think carefully in a palindrome, the elements left and right to the middle elements are same.
                >> We put pointer on the middle element using slow and fast pointer technique
                >> reverse linked list from mid till the end
                >> traverse the linkedlist from start and end until we reach the middle element
                >> compare the data 

                1 -> 2 -> 2 <-1 <- 2
                          |
                          v
                        None

                Time complexity = O(n)
                Space complexity = O(1)

"""
class Solution:
    def isPalindrome(self, head):
        
        # lets find the middle
        
        slow = head
        fast = head 
        
        while fast != None and fast.next != None:
            
            slow = slow.next
            fast = fast.next.next
            
        # slow pointer is at the middle
        middle = slow
        
        #Now we have to reverse the list from middle till end
        
        prev = None
        curr = middle
        head2 = None
        
        while curr != None:
            nextNode = curr.next
            
            if nextNode == None:
                head2 = curr
            
            curr.next = prev
            
            prev = curr 
            curr = nextNode
            
        curr1 = head
        curr2 = head2
        
        while curr1 != None and curr2 != None: # after crossing the mid element both curr1 and curr2 will become None
            if curr1.data != curr2.data:
                return False
            
            curr1 = curr1.next
            curr2 = curr2.next
            
        return True
            
        

