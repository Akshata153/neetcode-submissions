class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True

        for r in range(len(s)+1):
            for l in range(r):
                # print(f"{l}:{r}")
                if dp[l] and s[l:r] in wordDict:
                    # print(dp)
                    dp[r]=True
        return dp[-1]