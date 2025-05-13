class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        answer = 0

        dp = [0 for _ in range(26)]

        for c in s:
            dp[ord(c) - ord('a')] += 1

        for c in range(t):
            nxt = [0] * 26
            nxt[0] = dp[25]
            nxt[1] = (dp[25] + dp[0]) % 1_000_000_007
            for i in range(2, 26):
                nxt[i] = dp[i - 1]
            dp = nxt
        answer = sum(dp) % 1_000_000_007
        return answer


        


        