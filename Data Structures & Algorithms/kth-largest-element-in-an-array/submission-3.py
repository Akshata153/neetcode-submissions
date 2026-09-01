class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        stack=[]
        for n in nums:
            heapq.heappush(stack,n)
            if len(stack)>k:
                # print(stack[0])
                heapq.heappop(stack)
            
        return stack[0]
        
