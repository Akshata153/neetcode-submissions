class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen=defaultdict(int)
        for i,num in enumerate(nums):
            temp=target-num
            # print(seen)
            if temp in seen:
                return [seen[temp],i]
            seen[num]=i
             
            
        return [0,0]
