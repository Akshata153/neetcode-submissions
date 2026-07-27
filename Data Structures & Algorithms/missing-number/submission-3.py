class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res=0
        for n in range(len(nums)):
            res=res^(n+1)^nums[n]
        return res