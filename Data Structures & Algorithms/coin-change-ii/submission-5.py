class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp=[[-1]*(amount+1) for _ in range(len(coins))]
        def dfs(i,amt):
            if amt==0:
                return 1
            if i>=len(coins):
                return 0
            if dp[i][amt]!=-1:
                return dp[i][amt]
            
            ways=0
            if coins[i]<=amt:
                ways=dfs(i+1,amt)
                ways+=dfs(i,amt-coins[i])
            dp[i][amt]=ways
            return ways
        return dfs(0,amount)

