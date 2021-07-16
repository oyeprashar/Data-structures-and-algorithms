# postfix evaluation
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
def PostfixEval(list1):
    stack1 = Stack()
    operator = ['+', '-', '*', '^', '/']
    for char in list1:
        if not(char) in operator:
            stack1.push(char)
        else:
            top = str(stack1.pop())
            second = str(stack1.pop())
            
            item = second+char+top
            stack1.push(eval(item)) # eval(str) is used to evaluate expression which is given as a string not int
    
    return stack1.peek()
list1 = ['5','6','2','+','*','12','4','/','-']
print(PostfixEval(list1)) 
        
