class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minm=prices[0]
        profit=0
        for i in range(len(prices)):
            if prices[i]<minm:
                minm=prices[i]
            else:
                profit=max(profit,(prices[i]-minm))
        return profit