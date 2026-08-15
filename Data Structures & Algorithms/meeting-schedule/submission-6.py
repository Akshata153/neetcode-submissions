"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals)<=1:
            return True
        intervals.sort(key=lambda x:x.start)
        # print(intervals)
        prev=intervals[0].end
        i=1
        while i<len(intervals):
            # print(intervals[i].start)
            if intervals[i].start<prev:
                return False
            else:
                prev=max(intervals[i].end,prev)
            i+=1
        return True