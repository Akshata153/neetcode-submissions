class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count=defaultdict(int)
        longest=0
        l=0
        curr_freq_len=0
        for r in range(len(s)):
            count[s[r]]+=1
            curr_freq_len=max(curr_freq_len,count[s[r]])

            while (r-l+1)-curr_freq_len > k: #shrink
                count[s[l]]-=1
                l+=1
            #now willl have valid substring with replacement at this point in window
            longest=max(longest,r-l+1)
        return longest