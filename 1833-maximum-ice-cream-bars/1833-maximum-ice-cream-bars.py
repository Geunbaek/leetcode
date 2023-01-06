class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(len(costs)):
            if costs[i] <= coins:
                coins -= costs[i]
            else:
                return i
        return len(costs)
        