class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        stack=[]
        for n in nums:
            heapq.heappush(stack,-n)
        while k>1:
            heapq.heappop(stack)
            k-=1

            
        return -stack[0]
        
