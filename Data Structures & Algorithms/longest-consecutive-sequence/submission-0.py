class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0
        count=0
        for n in nums:
            if (n-1) not in s: #start of seq
                temp=n
                count=0
                while temp in nums:
                    count+=1
                    temp+=1
                longest=max(longest,count)

        return longest
                
