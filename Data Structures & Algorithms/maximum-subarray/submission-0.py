class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l=float('inf')
        h=float('-inf')
        maxm=nums[0]
        for i in range(len(nums)):
            l=min(nums[i],nums[i]+l,nums[i]+h)
            h=max(nums[i],nums[i]+l,nums[i]+h)
            maxm=max(maxm,h)
        return maxm