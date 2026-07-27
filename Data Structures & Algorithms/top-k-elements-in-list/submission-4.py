class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        # m=0
        heap=[]
        for n,c in count.items():
            heapq.heappush(heap,(c,n))
            if len(heap)>k:
                heapq.heappop(heap)
            
            # print(heap)
            # m+=1
        
        return [n for c,n in heap]