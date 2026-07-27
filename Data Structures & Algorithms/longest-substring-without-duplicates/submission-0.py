class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        maxm=0
        myset=set()
        for r in range (len(s)):
            if s[r]  in myset:
                
                while s[r] in myset:
                    myset.remove(s[l])
                    l+=1
            myset.add(s[r])
            maxm=max(maxm,r-l+1)
        return maxm