class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res=[]
        
        i=1
        # print(res)
        intervals.sort()
        res.append(intervals[0])
        # print(intervals)
        while i<len(intervals):
            # print(res)
            if res[-1][1]>=intervals[i][0]:
                res[-1][0]=min(intervals[i][0],res[-1][0])
                res[-1][1]=max(intervals[i][1],res[-1][1])
            else:
                res.append(intervals[i])
            i+=1
        return res