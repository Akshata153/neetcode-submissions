class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in nums[i+1:]:
                j=nums[i+1:].index(temp)+i+1
                return [i,j]
        return [0,0]