class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # heap (dist,[x,y])
        heap=[]
        for x,y in points:
            temp=math.sqrt(x*x+y*y)
            heapq.heappush(heap,[temp,x,y])
        # print(heap)
        res=[]
        while k:
            temp,x,y=heapq.heappop(heap)
            res.append([x,y])
            k-=1
        return res
