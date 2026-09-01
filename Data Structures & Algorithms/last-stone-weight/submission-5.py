class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones)==0:
            return 0
        if len(stones)==1:
            return stones[0]
        stack=[]
        for x in stones:
            heapq.heappush(stack,-x)
        # print(stack)
        while len(stack)>1:
            x=heapq.heappop(stack)
            y=heapq.heappop(stack)
            if x!=y:
                diff=abs(x-y)
                heapq.heappush(stack,-diff)
        return 0 if len(stack)==0 else -stack[0]