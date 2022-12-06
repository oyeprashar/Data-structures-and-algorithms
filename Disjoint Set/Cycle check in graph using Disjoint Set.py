#finding the cycle using optimized DSU

def find(element,parentList):
    if parentList[element] == -1:
        return element

    absoluteParent = find(parentList[element],parentList)
    parentList[element] = absoluteParent

    return absoluteParent


def union(element1,element2,rankList,parentList):
    parent1 = find(element1,parentList)
    parent2 = find(element2,parentList)

    if parent1 != parent2:
        if rankList[parent1] > rankList[parent2]:
            parentList[parent2] = parent1
            rankList[parent1] += rankList[parent2]

        else:
            parentList[parent1] = parent2
            rankList[parent2] += rankList[parent1]


def findCycleDSU(edgeList):
    rankList = [1] * len(edgeList)
    parentList = [-1] * len(edgeList)

    for pair in edgeList:
        v1 = pair[0]
        v2 = pair[1]

        parent1 = find(v1,parentList)
        parent2 = find(v2,parentList)

        print("checking for ", v1, "its parent =", parent1, "edge2 =", v2, "its parent2 =",parent2)

        if parent1 != parent2:
            # union(parent1,parent2,rankList,parentList)
            union(v1,v2,rankList,parentList)
            print(parentList)

        else:
            print("== cycle detected == for v1 =",v1,"its parent =",parent1,"v2 =",v2,"its parent2 =",parent2)

            return

    print("No cycle detected")



edgeList = [(0,1),(1,2),(2,3),(3,0)]
findCycleDSU(edgeList)