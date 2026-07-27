class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        res=[]
        l=0
        #maxheap
        for r in range(0,k-1):
            heapq.heappush(heap,-nums[r])
            heapq.heapify(heap)
        print(heap)
        for r in range(k-1,len(nums)):
            # print("heap:",heap)
            heapq.heappush(heap,-nums[r])
            heapq.heapify(heap)
            x=-heap[0]
            # print(x)
            res.append(x)
            heap.remove(-nums[l])
            # if nums[l]==x:

            # heapq.heappush(heap,-nums[l])
            # heapq.heapify(heap)
            l+=1
            
            

        return res
