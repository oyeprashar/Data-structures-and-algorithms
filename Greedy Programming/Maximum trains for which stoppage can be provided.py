class Item:
    def __init__(self, arr, dep, platNo):

        self.arr = arr
        self.dep = dep
        self.platNo = platNo
    
    def __lt__(self,otherObject):
        
        if self.platNo == otherObject.platNo:
            return self.dep < otherObject.dep
        else:
            return self.platNo < otherObject.platNo

def find(input_arr):

    objList = []
    
    for list1 in input_arr:
        arr = list1[0]
        dep = list1[1]
        platNo = list1[2]
        currObj = Item(arr,dep,platNo)
        objList.append(currObj)
    
    objList.sort()

    for item in objList:
        print(item.arr, item.dep, item.platNo)

    lastPlat = objList[0].platNo
    lastDep = objList[0].dep
    trains = 1

    # print(lastPlat,lastDep,trains)
    for i in range(1,len(objList)):

        # print("last Platform ==",lastPlat,"last departure time ==",lastDep,"trains accomodated ==",trains)

        obj = objList[i]
        currPlat = obj.platNo
        currArr = obj.arr
        currDep = obj.dep

        if currPlat == lastPlat:
            # print(1)
            if currArr > lastDep:
                # print(currArr,currDep,currPlat)
                trains += 1
                lastDep = currDep
        
        else:
            trains += 1
            lastPlat = currPlat
            lastDep = currDep
        
    return trains




arr = [[1000, 1030, 3], [1010, 1020, 1], [1025, 1040, 1], [1130, 1145, 2], [1130, 1140, 2]]
# arr1 = [[1000, 1030, 3], [1010, 1020, 1], [1025, 1040, 1], [1130, 1145, 2], [1130, 1140, 2]]
# arr2 = [[1000,1030,1], [1010,1030,1], [1000,1020,2], [1030,1230,2], [1200,1230,3], [900,1005,1]]
# arr2 = [[1000,1030,1], [1010,1030,2], [1000,1020,2], [1030,1230,2], [1200,1230,3], [900,1005,1]]
# print(find(arr1))
print(find(arr))