class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        n = len(customers)
        total = 0
        dp = [0]
        
        for c, g in zip(customers, grumpy):
            if g == 0:
                total += c
                dp.append(dp[-1])
                
            if g == 1:
                dp.append(dp[-1] + c)
        _max = 0    
        for i in range(minutes, n + 1):
            _max = max(_max, dp[i] - dp[i - minutes])
            
        return total + _max
        