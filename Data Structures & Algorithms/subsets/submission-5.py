class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def dfs(i,currlist):
            if i==len(nums):
                res.append(currlist.copy())
                return
            
            currlist.append(nums[i])
            dfs(i+1,currlist)
            currlist.pop()
            dfs(i+1,currlist)
        
        dfs(0,[])
        return res