class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)

        dp = [[0 for _ in range(n)] for _ in range(n)]

        values = {value: index for index, value in enumerate(arr)}

        answer = 0
        for cur in range(n):
            for prev1 in range(cur):
                diff = arr[cur] - arr[prev1]
                prev2 = values.get(diff, -1)
                if diff < arr[prev1] and prev2 > -1:
                    dp[cur][prev1] = dp[prev1][prev2] + 1
                else:
                    dp[cur][prev1] = 2
                answer = max(answer, dp[cur][prev1])
        return answer if answer > 2 else 0


