class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        myset=set(wordDict)
        dp[0]=True
        for r in range(len(s)+1):
            for l in range(r):
                if dp[l] and s[l:r] in myset:
                    dp[r]=True
        return dp[-1]
