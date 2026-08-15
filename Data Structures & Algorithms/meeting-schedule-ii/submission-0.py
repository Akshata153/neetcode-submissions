"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        heap=[]
        intervals.sort(key=lambda x:x.start)
        heapq.heappush(heap,intervals[0].end)

        i=1
        while i<len(intervals):
            if heap[0]<=intervals[i].start:
                heapq.heappop(heap)
            heapq.heappush(heap,intervals[i].end)
            i+=1
        return len(heap)
            

        