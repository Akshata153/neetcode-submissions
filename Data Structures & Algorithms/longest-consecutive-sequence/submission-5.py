class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        freq=defaultdict(int)
        maxm=float('-inf')
        nums.sort()
        for n in nums:
            if freq[n]:
                continue
            if n-1 in freq and freq[n]==0:
                freq[n]=freq[n-1]+1
                
            else:
                freq[n]=1
            maxm=max(maxm,freq[n])
            # print(f"{n}:{freq[n]}")

        return maxm

        