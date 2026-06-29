class Solution:

    def getLastNode(self, head):
        curr = head
        while curr.next is not None:
            curr = curr.next
        return curr

    def findPairsWithGivenSum(self, target, head):

        res = []
        lastNode = self.getLastNode(head)
        curr = head

        while curr != lastNode:

            if curr.data + lastNode.data == target:
                res.append([curr.data, lastNode.data])

                # because if we move the pointers, they will cross each other (left > right)
                if curr.next == lastNode:
                    return res

                curr = curr.next
                lastNode = lastNode.prev

            elif curr.data + lastNode.data < target:
                curr = curr.next

            else:
                lastNode = lastNode.prev

        return res
