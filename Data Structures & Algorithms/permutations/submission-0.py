class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(currlist):
            if len(currlist)==len(nums):
                res.append(currlist.copy())
                return 
            
            for n in nums:
                if n not in currlist:
                    currlist.append(n)
                    dfs(currlist)
                    currlist.pop()
        dfs([])
        return res