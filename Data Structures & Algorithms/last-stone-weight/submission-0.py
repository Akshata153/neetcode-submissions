class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heap=[]
        # 2 2 3 4 6
        heapq.heapify(stones)
        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)
            heapq.heappush(stones,-(abs(x-y)))
        
        stones.append(0)
            
        return -stones[0]