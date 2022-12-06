#User function Template for python3

'''
    :param head: head of unsorted linked list 
    :return: head of sorted linkd list
    
    # Node Class
    class Node:
        def __init__(self, data):  # data -> value stored in node
            self.data = data
            self.next = None
'''
class Solution:
    
    def findMid(self,curr):
        if curr.next.next == None:
            return curr
            
        slow = curr
        fast = curr
        
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
        
    def mergeSort(self, head):
        
        if head.next == None:
            return head
        
        
        mid = self.findMid(head)
        
        left = head
        
        right = mid.next
        mid.next =None
        
        left = self.mergeSort(left)
        right = self.mergeSort(right)


        newHead = None
        prev = None
        

        while left != None and right != None:
            
            if left.data < right.data:
                newNode = Node(left.data)
                
                if newHead == None:
                    newHead = newNode
                    prev = newNode
                    
                else:
                    prev.next = newNode
                    prev = newNode
                
                left = left.next
                
            else:
                
                newNode = Node(right.data)
                
                if newHead == None:
                    newHead = newNode
                    prev = newNode
                    
                else:
                    prev.next = newNode
                    prev = newNode
                
                right = right.next
                    
        while left != None:
            newNode = Node(left.data)
            prev.next = newNode
            prev = newNode
            left = left.next
            
            
        while right != None:
            newNode = Node(right.data)
            prev.next = newNode
            prev = newNode
            right = right.next
            
        return newHead
                
                    
                
                
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node

# prints the elements of linked list starting with head
def printList(head):
    if head is None:
        print(' ')
        return
    curr_node = head
    while curr_node:
        print(curr_node.data,end=" ")
        curr_node=curr_node.next
    print(' ')


