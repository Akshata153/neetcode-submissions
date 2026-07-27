class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        j=0

        for i,num in enumerate(nums):
            j=i+1
            while j<len(nums[i+1:]):
                temp=-(num+nums[j])
                if temp in nums[j+1:]:
                    if [num,nums[j],temp] not in res:
                        res.append([num,nums[j],temp])
                j+=1
            
        return res
