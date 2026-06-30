"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""



class Solution:
    def copyRandomList(self, head):

        if head is None:
            return head

        # step 1 : create new nodes
        curr = head
        while curr is not None:
            newNode = Node(curr.val)
            nextNode = curr.next
            curr.next = newNode
            newNode.next = nextNode
            curr = nextNode


        # step 2 : Make the random connections between new nodes
        curr = head
        while curr is not None:
            if curr.random is not None:
                curr.next.random = curr.random.next
            curr = curr.next.next


        # step 3 : remove the connection between the old and new nodes
        # IMP : We need to unlink both old and new nodes!
        
        curr = head
        newHead = head.next
        
        while curr is not None:
            
            newNode = curr.next
            curr.next = curr.next.next
            
            if newNode.next != None:
                newNode.next = newNode.next.next
                
            curr = curr.next
            
        return newHead
            

