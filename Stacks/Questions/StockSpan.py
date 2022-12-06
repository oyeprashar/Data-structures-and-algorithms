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
def StockSpan(price):
    stack1 = Stack()
    # n = len(price)
    span = []
    span.append(1) #span for first element is always 1
    stack1.push(0) # pushing index of first element i.e. 0
    for i in range(1,len(price)):
        if price[stack1.peek()] > price[i]:
            # to get the postive values in span list, we must compare the index before subtacting 
            # since we are comparing the values from the price list and not the indices hence negative values can occur if the indices are not compared before 
            # subtraction
            # no matter what stack top will be the index of last processed element in price list
            if stack1.peek() > i:
                current_span = stack1.peek() - i
                span.append(current_span)
                stack1.push(i)
            else:
                current_span = i - stack1.peek()
                span.append(current_span)
                stack1.push(i)
        elif price[i] > price[stack1.peek()]:
            while not(price[stack1.peek()]) > price[i]:
                stack1.pop()
            # to get positive values in the span list, we must compare the index before subtracting 
            if stack1.peek() > i:
                span.append(stack1.peek() - i)
                stack1.push(i)
            else:
                span.append(i - stack1.peek())
                stack1.push(i)
    return span
list1 = [100,80,60,70,60,75,85]
print(StockSpan(list1))

