class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n,m=0,0
        for i in range(len(nums)+1):
            n=n^i
        for i in range(len(nums)):
            m=m^nums[i]
        return n^m