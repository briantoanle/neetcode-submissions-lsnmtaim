"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        
        # sort input array
        # check if end1 > start2
        # return false
        length = len(intervals)
        for i in range(length):
            #print(intervals[i].start, intervals[i].end)
            intervals[i] = [intervals[i].start, intervals[i].end]
        []
        intervals.sort()
        #print(intervals)
        start = 0
        # [(5,8),(9,15)]
        for i in range( length- 1):
            #print('checking',intervals[i], 'and ',intervals[i+1])
            if intervals[i][1] > intervals[i+1][0]:
                return False

        return True
