class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        def count_zeroone(s):
            ret = [0, 0]
            for c in s:
                ret[ord(c) - ord("0")] += 1
            return ret


        for s in strs:
            count = count_zeroone(s)
            for z in range(m, count[0] - 1, -1):
                for o in range(n, count[1] - 1, -1):
                    dp[z][o] = max(1 + dp[z - count[0]][o - count[1]], dp[z][o])
        return dp[m][n]