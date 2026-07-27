class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res=[]
        l=0
        for r in range(k-1,len(nums)):
            i=l
            maxm=float('-inf')
            while i<=r:
                maxm=max(maxm,nums[i])
                i+=1
            res.append(maxm)
            l+=1
        return res