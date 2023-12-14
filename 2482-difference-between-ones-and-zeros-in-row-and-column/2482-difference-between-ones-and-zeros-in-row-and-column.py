class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        r = len(grid)
        c = len(grid[0])
        
        board = [[0 for _ in range(c + 1)] for _ in range(r + 1)]
        
        for y in range(r):
            for x in range(c):
                if grid[y][x] == 1:
                    board[y + 1][0] += 1
                    board[0][x + 1] += 1
                    
        ans = [[0 for _ in range(c)] for _ in range(r)]
        
        for y in range(r):
            for x in range(c):
                ans[y][x] = board[y + 1][0] + board[0][x + 1] - (r - board[y + 1][0] + c - board[0][x + 1])
        return ans
                
                    
                
        