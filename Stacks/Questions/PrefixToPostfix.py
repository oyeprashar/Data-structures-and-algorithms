class Stack():
    # defining the attributes
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not(self.isEmpty()):
            return self.items.pop()
        else: 
            return "UNDERFLOW"
    def peek(self):
        return self.items[len(self.items)-1]
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
def PrefixToPostfix(str1):
    str2 = str1[::-1]
    stack1 = Stack()
    operator = ['+','-','*','^','/']
    for char in str2:
        if not(char) in operator:
            stack1.push(char)
        else:
            top = stack1.pop()
            second = stack1.pop()
            item = top+second+char
            stack1.push(item)
    
    return stack1.peek()
print(PrefixToPostfix('+/+A^BD-EFG'))