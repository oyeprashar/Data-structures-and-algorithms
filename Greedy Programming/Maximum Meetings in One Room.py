class Solution:
    def maxMeetings(self, start, finish):

        meetings = []

        for i in range(len(start)):
            meetings.append([start[i], finish[i]])

        meetings.sort(key = lambda x :x[1])
        nonOverlappingMeetings = 1
        lastFinishTime = meetings[0][1]

        for i in range(1, len(meetings)):
            if meetings[i][0] >= lastFinishTime:
                nonOverlappingMeetings += 1
                lastFinishTime = meetings[i][1]

        return nonOverlappingMeetings
