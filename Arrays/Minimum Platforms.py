"""
We need to find the minimum number of platforms that can accommodate all the trains during the peak hour.
"""

class Solution:

    def minPlatform(self, arrival, departure):
        arrival.sort()
        departure.sort()

        peakTimePlatforms = 1
        currPlatforms = 1

        i = 1
        j = 0

        while i < len(arrival) and j < len(departure):

            # add a platform and let the train arrive
            if arrival[i] <= departure[j]:
                currPlatforms += 1
                i += 1  #

            # Trains departs and the platform is no longer needed
            else:
                currPlatforms -= 1
                j += 1

            # keep track of how many platforms were used during the peak/busiest hour
            peakTimePlatforms = max(peakTimePlatforms, currPlatforms)

        return peakTimePlatforms

