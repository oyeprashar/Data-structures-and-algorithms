"""
Approach :
    1. pop the first k element from the queue and into a stack
    2. pop the stack top and append the elements to the end of the same queue
    3. pop len(queue) - k elements and append to the end of the queue
"""



class Solution:
    def reverseFirstK(self, queue, k):

        if k > len(queue):
            return queue

        k = min(k, len(queue))
        stack = []
        nonReversedElements = len(queue) - k

        while len(queue) > 0 and k != 0:
            stack.append(queue.popleft())
            k -= 1

        while len(stack) > 0:
            queue.append(stack.pop())

        while nonReversedElements > 0:
            queue.append(queue.popleft())
            nonReversedElements -= 1

        return queue
