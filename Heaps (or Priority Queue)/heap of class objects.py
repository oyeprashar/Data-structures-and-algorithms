"""
overload __lt__  (called as rich comparator) this is used by the heapq.heapify to compare them and generate the heap

NOTE: after overloading rich comparator list of objects of this class can be sorted also
"""
import heapq

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __lt__(self, otherObject):
        return self.age < otherObject.age   # < is used for min heap

    # def __lt__(self, otherObject):
    #     return self.age > otherObject.age   # > is used for the max heap


p1 = Person("Shubham", 21)
p2 = Person("Shikha", 26)
p3 = Person("Pratima", 58)

list1 = [p3, p2, p1]

heapq.heapify(list1)
for element in list1:
    print(element.age, end=" ")
