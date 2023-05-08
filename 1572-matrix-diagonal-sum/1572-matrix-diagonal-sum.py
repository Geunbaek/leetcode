class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        _sum = 0
        
        for y in range(n):
            _sum += mat[y][y] + mat[y][(n - 1) - y]
            
        return _sum if n % 2 == 0 else _sum - mat[n // 2][n // 2]