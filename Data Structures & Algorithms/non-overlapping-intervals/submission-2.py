class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if len(intervals)<=1:
            return 0
        intervals.sort()
        i=1
        count=0
        # print(intervals)
        res=[]
        res.append(intervals[0])

        while i<len(intervals):
            if res[-1][1]>intervals[i][0]:
                # print(i)
                count+=1
                res[-1][1]=min(res[-1][1],intervals[i][1])
            else:
                res.append(intervals[i])
            i+=1
        return count