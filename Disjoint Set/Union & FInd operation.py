def find(element,parentArray):
    if parentList[element] == -1:
        return element
    return find(parentList[element],parentList)

def union(a,b,parentArray):
    parentOfa = find(a,parentList)
    parentOfb = find(b,parentList)
    parentList[parentOfa] = parentOfb

parentList = [0,-1,1,2,-1,4,6]
print(find(4,parentList))
print(parentList)
union(4,1,parentList)
print(parentList)
print(find(4,parentList))
