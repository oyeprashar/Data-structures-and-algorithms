"""
This is extremely simple. We just sort the data by departure time and then keep track of departure time at each
platform and just simply compare! Thats it!
"""

class Solution:
    def maxStop(self, m, trains):

        platforms = [None] * m
        trains.sort(key = lambda x : x[1])
        trainsServed = 0

        for train in trains:
            arrival = train[0]
            departure = train[1]
            requiredPlatform = train[2] - 1

            if requiredPlatform > len(platforms) - 1:
                continue

            platformDeparture = platforms[requiredPlatform]

            if platformDeparture is None or arrival >= platformDeparture:
                platforms[requiredPlatform] = departure
                trainsServed += 1

        return trainsServed
