class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        myset=set()
        for n in nums:
            if n in myset:
                return n
            myset.add(n)
        return 0