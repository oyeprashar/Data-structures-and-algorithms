class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not(self.isEmpty()):
            return self.items.pop()
        else:
            return 'UNDERFLOW'
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return  self.items == []
    def size(self):
        return len(self.items)
    
def PostfixToPrefix(str1):
    stack1 = Stack()
    operator = ['+','-','*','^','/']
    for char in str1:
        if not(char) in operator:
            stack1.push(char)
        else:
            top = stack1.pop()
            second = stack1.pop()
            item = char+second+top
            stack1.push(item)
    return stack1.peek()

print(PostfixToPrefix('AB+CD-*'))
        