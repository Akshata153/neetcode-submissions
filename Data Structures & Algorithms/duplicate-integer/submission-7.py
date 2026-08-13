class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp=defaultdict(int)
        for i in range(len(nums)):
            if mapp[nums[i]]:
                return True
            mapp[nums[i]]+=1
        return False