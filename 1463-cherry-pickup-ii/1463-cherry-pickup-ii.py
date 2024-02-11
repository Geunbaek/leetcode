class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r, c = len(grid), len(grid[0])
        memo = dict()
        
        def dp(row, col1, col2):
            if row >= r:
                return 0
            
            if not (0 <= col1 < c and 0 <= col2 < c):
                return 0
            
            if (row, col1, col2) in memo:
                return memo[(row, col1, col2)]
       
            ret = grid[row][col1]
            if col1 != col2:
                ret += grid[row][col2]
            
      
            _max = 0

            for next_col1 in [col1 - 1, col1, col1 + 1]:
                for next_col2 in [col2 - 1, col2, col2 + 1]:
                    _max = max(_max, dp(row + 1, next_col1, next_col2))

            ret += _max
            
            memo[(row, col1, col2)] = ret
            return memo[(row, col1, col2)]
        
        return dp(0, 0, c - 1)
            
            