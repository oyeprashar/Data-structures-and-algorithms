"""
Implement a max stack 

properties
1) return max in O(1) time and space
2) this max is maintained while we pope and append element to the stack
"""

class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxEle = None

    def push(self,data):    

        if len(self.stack) == 0:
            self.stack.append(data)
            self.maxEle = data

        elif data > self.maxEle:
            newData = 2*data - self.maxEle
            self.stack.append(newData)
            self.maxEle = data 

        else:
            self.stack.append(data)


    def pop(self):

        # pop is working fine now
        if len(self.stack) == 0:
            return "Stack is empty"

        elif self.stack[-1] > self.maxEle:
            orgValue = self.maxEle
            self.maxEle = self.maxEle*2 - self.stack[-1]
            self.stack.pop()
            return orgValue

        else:
            return self.stack.pop()


    # this will return the stack top
    def top(self):

        if len(self.stack) == 0:
            return "Error: stack is empty"

        elif self.stack[-1] > self.maxEle:
            return self.maxEle

        else:
            return self.stack[-1]


            