class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        nums.sort()
        dp={}
        # print(dp)
        def dfs(i,total):
            if i==len(nums) and total==target:
                return 1
            if i>=len(nums):
                return 0
            # print(total)
            if (i,total) in dp:
                return dp[(i,total)]
            res=0
            
            res=dfs(i+1,total+nums[i])
            res+=dfs(i+1,total-nums[i])
            dp[(i,total)]=res
            return res
        return dfs(0,0)
            