## Prefix to infix is like prefix to postfix only with a difference ki beech me operator lga ke push krna h stack me
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
    
def PrefixToInfix(str1):
    operators = ['+','-','*','^','/']
    str2 = str1[::-1]
    stack1 = Stack()
    for char in str2:
        if not(char) in operators:
            stack1.push(char)
        else:
            top = stack1.pop()
            second = stack1.pop()
            item = top+char+second
            stack1.push(item)

    return stack1.peek()
print(PrefixToInfix('*+ab/ef'))