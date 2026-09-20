class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(i,curr):
            if len(curr)==len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):
                if nums[j] in curr:
                    continue
                
                curr.append(nums[j])
                dfs(j+1,curr)
                curr.pop()
            
        dfs(0,[])
        return res