class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        def check(x, y):
            cnt =0 
            for ny in range(y, y + n):
                for nx in range(x, x + n):
                    if img1[ny - y][nx - x] == 1 and board[ny][nx] == 1:
                        cnt += 1
            return cnt
        
        n = len(img1)
        
        board = [[0 for _ in range(3 * n)] for _ in range(3 * n)]
        ans = 0

        for y in range(n, 2 * n):
            for x in range(n, 2 * n):
                board[y][x] = img2[y - n][x - n]

        for y in range(2 * n):
            for x in range(2 * n):
                ans = max(ans, check(x, y))

        return ans