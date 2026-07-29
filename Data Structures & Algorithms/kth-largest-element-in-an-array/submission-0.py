class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heap=[s for s in nums[:k]]
        heapq.heapify(heap)
        for n in nums[k:]:
            # print(heap)
            heapq.heappush(heap,n)
            
            while len(heap)>k:
                heapq.heappop(heap)
        # print(heap)
        return heap[0]
