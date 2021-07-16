def find(i, parentList):
    if parentList[i] == -1:
        return i
    parentList[i] = find(parentList[i], parentList)
    return parentList[i]


parentList = [-1, 7, 1, 2, 7, 4, 5, -1]
            #[-1, 7, 7, 7, 7, 4, 5, -1]
print(find(3, parentList))
print(parentList)


