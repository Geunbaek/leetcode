class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        r, c = len(mat), len(mat[0])
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for y in range(1, r + 1):
            for x in range(1, c + 1):
                dp[y][x] = dp[y][x - 1] + mat[y - 1][x - 1]
        
        answer = 0
        for x in range(1, c + 1):
            for y in range(1, r + 1):
                dp[y][x] += dp[y - 1][x]
        
        for y in range(1, r + 1):
            for x in range(1, c + 1):
                l = 0
                while 1:
                    if not (x + l < c + 1 and y + l < r + 1):
                        break
                    area = dp[y + l][x + l] - dp[y + l][x - 1] - dp[y - 1][x + l] + dp[y - 1][x - 1]
                    if area <= threshold:
                        answer = max(answer, l + 1)
                    l += 1

        return answer