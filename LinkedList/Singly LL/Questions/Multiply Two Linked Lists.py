class Node:
    def __init__(self, key):
        self.data = key
        self.next = None

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

    def generateNumber(self, head):

        place = 1
        number = 0
        curr = head

        while curr is not None:
            number += (place * curr.data)
            curr = curr.next
            place *= 10

        return number


    def multiplyTwoLists(self, first, second):

        reversedHead1 = self.reverse(first)
        reversedHead2 = self.reverse(second)

        num1 = self.generateNumber(reversedHead1)
        num2 = self.generateNumber(reversedHead2)

        return num1 * num2
