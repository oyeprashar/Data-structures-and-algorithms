class Node:
    def __init__(self,data,value):
        self.data = data
        self.value = value
        self.next = None
        self.prev = None
         
class LRUCache:

    def __init__(self, cap: int):
        self.dictionary = {}
        self.cap = cap
        self.head = Node(None,None)
        self.tail = Node(None,None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        
        if key in self.dictionary:
            
            ans = self.dictionary[key].value
            self.move_to_start(key)
            return ans 

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        
        if key in self.dictionary:
            
            self.dictionary[key].value = value 
            self.move_to_start(key)
        
        else: 
            
            if len(self.dictionary) < self.cap:
                self.add_entry(key,value)
              
            elif len(self.dictionary) == self.cap:
                
                self.remove_entry()
                self.add_entry(key,value)
            
            
    def move_to_start(self,key):
        currNode  = self.dictionary[key] 
        
        # step 1: Remove from the old position
        currNode.prev.next = currNode.next 
        currNode.next.prev = currNode.prev 

        # step1 : add this node at the start
        currNode.next = self.head.next 
        self.head.next.prev = currNode 
        self.head.next = currNode
        currNode.prev = self.head 
    
    def add_entry(self,key,value):
        
        newNode = Node(key,value)
        self.dictionary[key] = newNode
        
        newNode.next = self.head.next
        self.head.next.prev = newNode
        self.head.next = newNode
        newNode.prev = self.head
        
    def remove_entry(self):
        currNode = self.tail.prev 
        self.dictionary.pop(currNode.data)
        currNode.prev.next = currNode.next
        currNode.next.prev = currNode.prev


# This is a correct and nice approach but interview might not like this and would ask me to code the LRU by DLL and hashmap
# from collections import OrderedDict

# class LRUCache:
      
#     #Constructor for initializing the cache capacity with the given value.  
#     def __init__(self,cap):
#         self.cap = cap
#         self.cache = OrderedDict()
        
        
#     #Function to return value corresponding to the key.
#     def get(self, key):
#         if key in self.cache:
#             self.cache.move_to_end(key)
#             return self.cache[key]
        
#         else:
#             return -1
        
#     def set(self, key, value):
        
#         if key in self.cache:
#             self.cache[key] = value
#             self.cache.move_to_end(key)
            
#         elif key not in self.cache:
#             if len(self.cache) < self.cap:
#                 self.cache[key] = value
#             else:
#                 self.cache.popitem(last=False)
#                 self.cache[key] = value
        
            