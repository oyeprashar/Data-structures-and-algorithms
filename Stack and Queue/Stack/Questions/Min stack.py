class MinStack:
    
    def __init__(self):
        self.stack = []
        self.minVal = None

    """
    @param: number: An integer
    @return: nothing
    """
    def push(self, number):
        
        if len(self.stack)  == 0:
            self.stack.append(number)
            self.minVal = number
        
        elif number < self.minVal:
            newNum = 2*number - self.minVal
            self.stack.append(newNum)
            self.minVal = number
        
        else:
            self.stack.append(number)
            

    """
    @return: An integer
    """
    def pop(self):
        
        if self.stack[-1] < self.minVal:
            newMin =  2*self.minVal - self.stack[-1]
            oldValue = self.minVal
            self.minVal = newMin
            self.stack.pop()
            return oldValue
            
        
        else:
            return self.stack.pop()


    """
    @return: An integer
    """
    def min(self):
        return self.minVal
