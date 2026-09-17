class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

def buildTestCase1Tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)
    return root

class Solution:
    def zigZagTraversal(self, root):

        queue = [root]
        currLevel = [root.data]
        ordering = []
        flag = 0

        while queue:

            if flag % 2 == 0:
                ordering.extend(currLevel)
            else:
                ordering.extend(currLevel[::-1])

            flag += 1
            currLevel = []

            for _ in range(len(queue)):

                curr = queue.pop(0)

                if curr.left is not None:
                    queue.append(curr.left)
                    currLevel.append(curr.left.data)

                if curr.right is not None:
                    queue.append(curr.right)
                    currLevel.append(curr.right.data)

        return ordering


root = buildTestCase1Tree()
s = Solution()
print(s.zigZagTraversal(root))

