# Rank of each node is 1
# When we make sets and assign parent then the rank changes or increments
def find(element, parentList):
    if parentList[element] == -1:
        return element
    parentList[element] = find(parentList[element], parentList)
    return parentList[element]


def union(item1, item2, rank, parentList):
    parentofItem1 = find(item1, parentList)
    parentofItem2 = find(item2, parentList)

    if parentofItem1 != parentofItem2:  # if already the both elements belong to the same set then we don't have to do anything
        if rank[parentofItem1] > rank[parentofItem2]:
            parentList[parentofItem2] = parentofItem1
            rank[parentofItem1] += rank[parentofItem2]
        else: # this else includes both bases when rank of parentofItem1 < parentofItem2 and when rank of both parents are equal
            parentList[parentofItem1] = parentofItem2
            rank[parentofItem2] += rank[parentofItem1]


