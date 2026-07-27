class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mymap={}
        for i in range(len(nums)):
            temp=target-nums[i]
            if temp in mymap:
                return [mymap[temp],i]
            mymap[nums[i]]=i
        return [0,0]