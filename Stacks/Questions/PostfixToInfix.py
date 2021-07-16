# postfix to infix is like prefix to infix bass the difference is that string is read from right to left in this case

class Stack():
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
    
def PostfixToInfix(str1):
    operator = ['+','-','*','^','/']
    stack1 = Stack()
    for char in str1:
        if not(char) in operator:
            stack1.push(char)
        else:
            top = stack1.pop()
            second = stack1.pop()
            item = top+char+second
            stack1.push(item)
    str2 = stack1.peek()
    print(str2[::-1])
    
PostfixToInfix('ab+ef/*')
