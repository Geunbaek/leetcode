class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        answer = 0

        for price in prices[::-1]:
            while stack and stack[-1] < price:
                stack.pop()
            if stack:
                answer = max(answer, stack[0] - price)
            stack.append(price)
        return answer