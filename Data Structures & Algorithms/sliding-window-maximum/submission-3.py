class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap=[]
        res=[]
        # for i in range(0,k):
        #     heapq.heappush(heap,(-nums[i],i))
        heap=[(-nums[i],i) for i in range(k-1)]
        heapq.heapify(heap)
        
        for r in range(k-1,len(nums)):
            heapq.heappush(heap,(-nums[r],r))
            # print(heap)

            while heap[0][1]<=(r-k):
                # print("pop: ",)
                # print(heap[0][1])
                x=heapq.heappop(heap)
                # print("pop: ",x)

            res.append(-heap[0][0])
            # print(f"res:{res}")

        return res

