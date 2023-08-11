class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0 for _ in range(amount + 1)] for _ in range(len(coins))]
        
        for y in range(len(coins)):
            dp[y][0] = 1
        
        for y, coin in enumerate(coins):
            for x in range(amount + 1):
                if coin > x:
                    dp[y][x] = dp[y - 1][x]
                else:
                    dp[y][x] = dp[y - 1][x] + dp[y][x - coin]
    
        return dp[-1][-1]
            
        