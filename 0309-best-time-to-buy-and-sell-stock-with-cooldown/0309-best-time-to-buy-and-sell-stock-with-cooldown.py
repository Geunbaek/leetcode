class Solution:
     def maxProfit(self, prices: List[int]) -> int:
        dp=[[0 for i in range(len(prices) + 2)] for j in range(2)]    
        
        for x in range(len(prices) - 1, -1, -1):
            dp[1][x] = max(-prices[x] + dp[0][x + 1] , dp[1][x + 1])
            dp[0][x] = max(prices[x] + dp[1][x + 2], dp[0][x + 1])
                    
        return dp[1][0]