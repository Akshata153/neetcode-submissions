class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxheap=[]
        for i in range(k):
            heapq.heappush(maxheap,(-nums[i],i))
        # print(maxheap)
        res=[]
        res.append(-maxheap[0][0])
        j=k
        while j<len(nums):
            heapq.heappush(maxheap,(-nums[j],j))
            while j-maxheap[0][1]+1>k:
                heapq.heappop(maxheap)
            
            res.append(-maxheap[0][0])
            j+=1
            
            
            # j+=1
        return res

            
