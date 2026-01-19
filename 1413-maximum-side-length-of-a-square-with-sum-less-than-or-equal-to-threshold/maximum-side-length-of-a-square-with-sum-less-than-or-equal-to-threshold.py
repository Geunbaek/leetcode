class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        def is_valid(k):
            for y in range(1, r + 1):
                for x in range(1, c + 1):
                    if not (x + k < c + 1 and y + k < r + 1):
                        continue
                    area = dp[y + k][x + k] - dp[y + k][x - 1] - dp[y - 1][x + k] + dp[y - 1][x - 1]
                    if area <= threshold:
                        return True
            return False

        r, c = len(mat), len(mat[0])
        dp = [[0 for _ in range(c + 1)] for _ in range(r + 1)]

        for y in range(1, r + 1):
            for x in range(1, c + 1):
                dp[y][x] = dp[y][x - 1] + mat[y - 1][x - 1]
        
        answer = 0
        for x in range(1, c + 1):
            for y in range(1, r + 1):
                dp[y][x] += dp[y - 1][x]
        
        left, right = 0, min(r, c) + 1

        while left <= right:
            mid = (left + right) // 2 

            if is_valid(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left