class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        stack=[]
        for p in points:
            dist=math.sqrt(pow(p[0],2)+pow(p[1],2))
            heapq.heappush(stack,(dist,(p[0],p[1])))
        
        res=[]
        while k:
            d,p=heapq.heappop(stack)
            res.append([p[0],p[1]])
            k-=1
        return res