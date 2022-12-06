"""
Input:
1
4
4 4
5 2
11 5
15 10
25 10

Output:
2

The algo is ki first we check if current fuel se we can reach the town. Agar we can then break and return the stop count. Else outta the all the reachable fuel stops
pick the stop with highest fuel capacity

1
1
4 4
25 10
"""
import heapq

class FuelPump:
    def __init__(self,dist,fuel,visited = False):
        self.dist = dist
        self.fuel = fuel
        self.visited = visited


    def __lt__(self,otherObject):
        return self.fuel > otherObject.fuel

# <- TAKING INPUTS AND SHIT HERE->
test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    fuelPumps = []
    for i in range(n):
        dist,fuel = map(int,input().split())
        fuelPumps.append([dist,fuel])
    totalDist, initialFuel = map(int,input().split())

    pumps = []
    for i in range(len(fuelPumps)):
        currFuel = fuelPumps[i][1]
        distFromTown = fuelPumps[i][0]
        currDist = totalDist - distFromTown
        currObj = FuelPump(currDist,currFuel)
        pumps.append(currObj)

    # pumps = sorted(pumps)
    # for pump in pumps:
    #     print("dist =",pump.dist," fuel =",pump.fuel)
    res = 0

    # remainingDist = totalDist
    currRange = initialFuel
    fuelTank = initialFuel
    remainingDist = totalDist
    visited = set()
    prevPumpDist = 0
    while totalDist > currRange:
        maxHeap = []

        for pump in pumps:
            if pump.dist <= currRange and pump.dist not in visited:
                # print(pump.dist,pump.fuel)
                heapq.heappush(maxHeap,pump)


        if len(maxHeap) == 0:
            res = -1
            break

        top = maxHeap[0]
        visited.add(top.dist)
        distTravelled = abs(top.dist - prevPumpDist) # abs because we may travel backward too, and uss case me bhi we waana subtract it from fuelTank
                                                     # warna - - (minus minus) = + (plus) hojayega
        fuelTank -= distTravelled
        fuelTank += top.fuel

        res += 1
        currRange = fuelTank + top.dist

        # for pump in pumps:
        #     if pump.dist <= top.dist:
        #         visited.add(pump.dist)
        prevPumpDist = top.dist
        print("selected fuel pump dist from start = ",top.dist," fuel picked up =",top.fuel,"fuelTank =",fuelTank," currRange =",currRange," distTravelled =",distTravelled," visited =",visited)

    print(res)




