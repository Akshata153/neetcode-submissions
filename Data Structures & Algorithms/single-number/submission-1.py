class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dt=Counter(nums)


        for v,c in dt.items():
            if c==1:
                return v
            
        
        return 0
