class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)//2
        dp=[False]*(target+1)
        dp[0]=True
        if sum(nums)%2:#odd
            return False

        for n in nums:
            for i in range(target,n-1,-1):
                dp[i]=dp[i] or dp[i-n]
        return dp[target]