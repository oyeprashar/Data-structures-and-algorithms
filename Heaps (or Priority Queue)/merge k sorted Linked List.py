import heapq


class Item:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

    def __lt__(self, otherObject):
        return self.data < otherObject.data


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        minHeap = []

        for i in range(len(lists)):
            firstNode = lists[i]
            if firstNode == None:
                continue
            data = firstNode.val
            nextNode = firstNode.next
            obj = Item(data, nextNode)
            heapq.heappush(minHeap, obj)

        head = None
        prev = None

        while len(minHeap) != 0:
            # IMPORTANT
            # top is object of class Item
            # top.next is object of class Node
            top = heapq.heappop(minHeap)
            currData = top.data
            print(currData)

            newNode = ListNode(currData, None)
            if prev == None:
                prev = newNode
                head = prev
            else:
                prev.next = newNode
                prev = newNode

            if top.nextNode is not None:
                currNode = top.nextNode
                itsData = currNode.val
                newNextNode = currNode.next
                top.data = itsData
                top.nextNode = newNextNode
                heapq.heappush(minHeap, top)

        return head