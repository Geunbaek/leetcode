class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        dp = [1 for _ in range(1_000_001)]
        dp[1] = 0
        for i in range(2, 1_000_001):
            if dp[i] == 0:
                continue
            
            for j in range(i + i, 1_000_001, i):
                dp[j] = 0
        
        stack = []
        answer = []

        for i in range(left, right + 1):
            if not dp[i]: continue

            stack.append(i)
            
            if len(stack) >= 2:
                answer.append((stack[-1] - stack[-2], stack[-2], stack[-1]))

        answer.sort()

        if answer:
            return answer[0][1:]
        return [-1, -1]