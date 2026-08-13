"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res=[[]]
        if len(intervals)<=0:
            return True
        intervals.sort(key=lambda x:x.start)
        res.append(intervals[0])
        # print(res)

        for i in range(1,len(intervals)):
            s=intervals[i]
            r=res[-1]
            # print(s)
            if not r.start<=s.start or r.end>s.start:
                return False
            res.append(intervals[i])
        return True
            