class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        myset=set(nums)
        maxn=0
        for n in myset:
            temp=n
            if n-1 not in myset:#new seq
                length=1
                while temp+1 in myset:
                    length+=1
                    temp+=1
                maxn=max(length,maxn)
        return maxn