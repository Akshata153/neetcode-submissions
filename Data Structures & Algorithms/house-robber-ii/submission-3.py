class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        
        def dfs(arr):
            if len(arr)==1:
                return arr[0]
            prevprev=arr[0]
            prev=max(arr[0],arr[1])

            for i in range(2,len(arr)):
                arr[i]=max(prevprev+arr[i],prev)
                
                prevprev=prev
                prev=arr[i]
            

            
            return arr[-1]

        return max(dfs(nums[:-1]),dfs(nums[1:]))