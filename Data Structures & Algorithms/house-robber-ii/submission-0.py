class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums)==1:
            return nums[0]
        res1=nums[:-1]
        res2=nums[1:]
        res1.append(0)
        l=len(res1)
        for i in range(l-4,-1,-1):
            res1[i]+=max(res1[i+2],res1[i+3])
        res1[0]=max(res1[0],res1[1])

        res2.append(0)
        l=len(res2)
        for i in range(l-4,-1,-1):
            res2[i]+=max(res2[i+2],res2[i+3])
        res2[0]=max(res2[0],res2[1])

        return max(res1[0],res2[0])