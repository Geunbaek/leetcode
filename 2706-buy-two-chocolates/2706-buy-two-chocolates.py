class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        
        sum = prices[0] + prices[1]
        
        return money - sum if sum <= money else money
        