class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        
        
        def dfs(i,currlist,l):
            if currlist not in res:
                res.append(currlist.copy())
                
            
            if l>=len(nums) or i>=len(nums):
                return
            
            # res.append(currlist.copy())

            currlist.append(nums[i])
            dfs(i+1,currlist,l+1)
            
            currlist.pop()
            dfs(i+1,currlist,l)
            return
        dfs(0,[],0)
        return res
