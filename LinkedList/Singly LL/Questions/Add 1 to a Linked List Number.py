class Node:
    def __init__(self, data):
        self.next = None
        self.data = data

class Solution:

    def reverse(self, head):

        curr = head
        prev = None

        while curr is not None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode

        return prev


    def addOne(self, head):

        reversedHead = self.reverse(head)
        curr = reversedHead
        carry = 1
        prev = None


        while curr is not None:

            currNum = curr.data

            print("curr data : ", currNum)

            total = currNum + carry

            print("carry was :", carry, " and total :", total)

            if total <= 9:
                print("if was executed")
                curr.data = total
                carry = 0
            else:
                carry = 1
                curr.data = 0

            if carry == 0:
                break

            prev = curr
            curr = curr.next

        if carry != 0:
            newNode = Node(carry)
            prev.next = newNode

        return self.reverse(reversedHead) # prev is None for some reason

def printLinkedList(head):
    print("checking the data")
    string = ""
    while head is not None:
        string += str(head.data)
        head = head.next
    return string


head = Node(4)
head.next = Node(5)
head.next.next = Node(6)
# print(printLinkedList(head))
s = Solution()
newHead = s.addOne(head)
# print(printLinkedList(newHead))












