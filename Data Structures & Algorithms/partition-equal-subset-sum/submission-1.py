class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target=sum(nums)//2
        myset=set()
        myset.add(0)

        for n in nums:
            tempset=set()
            for s in myset:
                temp=n+s
                if temp==target:
                    return True
                tempset.add(temp)
            myset.update(tempset)
        return False

