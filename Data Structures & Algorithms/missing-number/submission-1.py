class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hmap=defaultdict(int)
        for i in range(len(nums)):
            hmap[nums[i]]+=1
        for i in range(len(nums)):
            if hmap[i]==0:
                return i
        return len(nums)