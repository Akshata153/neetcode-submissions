class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            if len(nums)==1:
                return False
            x=nums[0]
            nums.sort()
            for n in nums[1:]:
                if n==x:
                    return True
                # print(f"{x} {n}")
                x=n

        return False