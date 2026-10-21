class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=nums[0]
        currmin,currmax=1,1

        for n in nums:
            temp=n*currmax
            currmax=max(n*currmax,n*currmin,n)
            currmin=min(temp,n*currmin,n)
            res=max(res,currmax)
            # print(f"{currmax} {currmin} {res}")
        return res