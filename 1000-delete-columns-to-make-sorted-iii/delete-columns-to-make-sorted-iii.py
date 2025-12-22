class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        c = len(strs[0])
        dp = [1 for _ in range(c)]

        for i in range(c - 2, -1, -1):
            for j in range(i + 1, c):
                is_valid = True
                for row in strs:
                    if row[i] > row[j]:
                        is_valid = False
                        break
                if is_valid:
                    dp[i] = max(dp[i], 1 + dp[j])
        return c - max(dp)