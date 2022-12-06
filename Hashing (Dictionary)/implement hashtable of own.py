class Node:
	def __init__(self,key,value):
		self.key = key
		self.value = value
		self.next = None
		self.prev = None


class MyHashMap:

    def __init__(self,capacity):

        self.capacity = capacity
        self.list = [None] * self.capacity

        
    # put updates the existing value as well
    def put(self, key: int, value: int) -> None:

        index = key % self.capacity

        if self.list[index] == None:
            self.list[index] = Node(key,value)

        else:
            curr = self.list[index]
            while curr.key != key and curr.next != None:
                curr = curr.next
                
            if curr.key == key:
                curr.value = value
                return

            newNode = Node(key,value)
            curr.next = newNode
            newNode.prev = curr
        

    def get(self, key: int) -> int:
        
        index = key % self.capacity

        if self.list[index] == None:
            return -1

        else:
            curr = self.list[index]

            while curr != None:
                if curr.key == key:
                    return curr.value
                curr = curr.next

            return -1
        

    def remove(self, key: int) -> None:
        
        index = key % self.capacity

        if self.list[index] == None:
            return 

        curr = self.list[index]

        while curr != None:
            if curr.key == key:

                """
                Location of nodes that can be removed
                1. only one node exists there
                3. the head or the first node
                3. any generic node
                """

                # case1: only one node is there
                if curr.next == None:
                    self.list[index] = None
                    
                # case2: we want to remove the first node
                elif curr.prev == None:
                    newHead = curr.next
                    self.list[index] = newHead 
                    newHead.prev = None

                # case3: removing any generic node

                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev

                return
