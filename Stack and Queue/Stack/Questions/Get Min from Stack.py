class SpecialStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # keep stack of min so far

    # push(x) – Insert an integer x into the stack.
    def push(self, data):

        if len(self.minStack) == 0 or data <= self.minStack[-1]:
            self.minStack.append(data)

        self.stack.append(data)

    # pop() – Remove the top element from the stack.
    def pop(self):

        if len(self.stack) == 0:
            return

        if self.minStack[-1] == self.stack[-1]:
            self.minStack.pop()

        return self.stack.pop()

    # peek() – Return the top element from the stack. If the stack is empty, return -1.
    def peek(self):

        if len(self.stack) == 0:
            return -1

        return self.stack[-1]

    # isEmpty() –  Return true if stack is empty, else false
    def isEmpty(self):
        return len(self.stack) == 0

    # getMin() – Retrieve the minimum element from the stack in O(1) time. If the stack is empty, return -1.
    def getMin(self):

        if len(self.minStack) == 0:
            return -1

        return self.minStack[-1]
