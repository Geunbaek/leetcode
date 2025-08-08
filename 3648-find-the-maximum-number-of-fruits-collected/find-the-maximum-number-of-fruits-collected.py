def is_lower(pos):
    x, y = pos
    return y > x

def is_upper(pos):
    x, y = pos
    return x > y


class Solution:
    def maxCollectedFruits(self, fruits: List[List[int]]) -> int:
        def get_max_fruits():
            dp[n - 1][0] = fruits[n - 1][0]
            dp[0][n - 1] = fruits[0][n - 1]
            dx = [1, 1, 1]
            dy = [-1, 0, 1]

            for x in range(n):
                for y in range(n - 1, n - x - 2, -1):
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue

                        if not is_lower((nx, ny)):
                            continue

                        dp[ny][nx] = max(dp[ny][nx], dp[y][x] + fruits[ny][nx])
            
            dx = [-1, 0, 1]
            dy = [1, 1, 1]
            for y in range(n):
                for x in range(n - 1, n - y - 2, -1):
                    for i in range(3):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if not (0 <= nx < n and 0 <= ny < n):
                            continue

                        if not is_upper((nx, ny)):
                            continue

                        dp[ny][nx] = max(dp[ny][nx], dp[y][x] + fruits[ny][nx])

        
        n = len(fruits)
        
        dp = [[0 for _ in range(n)] for _ in range(n)]
        dp[0][0] = fruits[0][0]

        for i in range(n):
            dp[i][i] = dp[i - 1][i - 1] + fruits[i][i]

        get_max_fruits()
        
        for l in dp:
            print(l)
        return dp[n - 1][n - 1] + dp[n - 1][n - 2] + dp[n - 2][n - 1]

       