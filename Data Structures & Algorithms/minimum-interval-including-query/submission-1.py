class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        res={}
        i=0
        minHeap=[]
        # print(intervals)
        for q in sorted(queries):
            # print(q)
            #push all valid : l<=q
            while i<len(intervals) and intervals[i][0]<=q:
                l,r=intervals[i]
                heapq.heappush(minHeap,((r-l+1),r))
                i+=1
            
            #pop all invalid : r<q
            while minHeap and minHeap[0][1]<q:
                # print(minHeap)
                # print(f"pop :{minHeap[0]}")
                heapq.heappop(minHeap)

            res[q]=minHeap[0][0] if minHeap else -1
        return [res[q] for q in queries]
