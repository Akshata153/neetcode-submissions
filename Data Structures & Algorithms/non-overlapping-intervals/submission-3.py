class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<=1:
            return 0
        intervals.sort()
        i=1
        count=0
        # print(intervals)
        prevEnd=intervals[0][1]

        while i<len(intervals):
            if prevEnd>intervals[i][0]:
                # print(i)
                count+=1
                prevEnd=min(prevEnd,intervals[i][1])
            else:
                prevEnd=intervals[i][1]
            i+=1
        return count