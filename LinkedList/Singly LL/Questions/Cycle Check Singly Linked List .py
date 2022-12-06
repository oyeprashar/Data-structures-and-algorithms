# Cycle check singly linked list
# logic is that we will have two loop variable marker1 and marker2. Both will start from the initial node and start traversing. Marker1 will move one node at and time
# whereas marker2 will move two nodes at a time. So this will make marker2 to traverse faster than marker1. If there is a loop in the linked list, there would be a time 
# where marker2 will be on the same node as the marker1 so will will return True else we will return False.

class Node():
    # defining the attributes
    def __init__(self,value):
        self.value = value
        self.nextnode = None


# # LL with loop (Output = True)
a = Node(1)
b = Node(2)
c = Node(3)

a.nextnode = b
b.nextnode = c
c.nextnode = a # Cycle Here!

# LL without loop (Output = False)
x = Node(1)
y = Node(2)
z = Node(3)

x.nextnode = y
y.nextnode = z # no cycle here

def cycle_check(node):
    # both marker1 and marker2 starts from the given node
    marker1 = node
    marker2 = node

    while marker2.nextnode != None:
        marker1 = marker1.nextnode
        marker2 = marker2.nextnode.nextnode

        if marker2 == marker1:
            return True
        
    return False
print(cycle_check(a))
print(cycle_check(x))
