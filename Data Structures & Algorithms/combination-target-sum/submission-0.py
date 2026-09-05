class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]

        def dfs(i,currlist,total):
            if total==target:
                res.append(currlist.copy())
                return
            if i>=len(nums) or total>target:
                return
            currlist.append(nums[i])
            dfs(i,currlist,total+nums[i])
            currlist.pop()
            dfs(i+1,currlist,total)
        dfs(0,[],0)
        return res