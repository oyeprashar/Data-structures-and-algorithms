class Solution:
    def DFS(self,currNode, value2Add, visited, head):
        
        visited.add(currNode)
        
        if currNode.val not in value2Add:
            newNode = Node(currNode.val)
            value2Add[currNode.val] = newNode
            
        currCloneNode = value2Add[currNode.val]
        
        if head[0] == None:
            head[0] = currCloneNode
        
        
        list1 = []
        for nbr in currNode.neighbors:
            
            if nbr.val not in value2Add:
                newNode = Node(nbr.val)
                value2Add[nbr.val] = newNode
            
            nbrCloneNode = value2Add[nbr.val]
            
            list1.append(nbrCloneNode)
            
            if nbr not in visited:
                
                self.DFS(nbr, value2Add, visited, head)
        
        currCloneNode.neighbors = list1
                
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if node == None:
            return None
        
        value2Add = {}
        visited = set()
        head = [None]
        
        self.DFS(node, value2Add, visited,head)
        
    
        return head[0]