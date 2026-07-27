class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict=defaultdict(int)

        for n in nums:
            if mydict[n]:
                return True
            mydict[n]+=1
        return False
