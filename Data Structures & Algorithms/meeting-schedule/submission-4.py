"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # res=(0,0)
        if len(intervals)<=0:
            return True
        intervals.sort(key=lambda x:x.start)
        res=intervals[0]
        # print(res)

        for i in range(1,len(intervals)):
            s=intervals[i]
            
            # print(s)
            # res.start<=s.start is redundant. cuz u already sorted. it is always true  :::: if not res.start<=s.start or res.end>s.start:
            if res.end>s.start:
                return False
            res=intervals[i]
        return True
            