class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        _min = prices[0]
        answer = 0
        
        for i in range(1, len(prices)):
            _min = min(_min, prices[i])
            answer = max(answer, prices[i] - _min)
            
        return answer
        