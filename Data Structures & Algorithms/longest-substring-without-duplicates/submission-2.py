class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxm=0
        i=0
        myset=set()
        for j in range(len(s)):
            while s[j] in myset:
                myset.discard(s[i])
                i+=1
            myset.add(s[j])
            maxm=max(maxm,j-i+1)
        return maxm