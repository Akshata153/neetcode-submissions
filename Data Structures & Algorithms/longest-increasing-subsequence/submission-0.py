class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp=[1]*len(nums)

        for r in range(len(nums)):
            for l in range(r):
                if nums[r]>nums[l]:
                    dp[r]=max(dp[r],dp[l]+1)
        return max(dp)