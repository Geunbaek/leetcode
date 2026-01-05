class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        h = []
        _sum = 0
        minus_sum = 0

        r,c = len(matrix), len(matrix[0])
        abs_min = float('inf')
        minus = []
        for y in range(r):
            for x in range(c):
                if matrix[y][x] >= 0:
                    _sum += matrix[y][x]
                else:
                    minus.append(matrix[y][x])
                abs_min = min(abs_min, abs(matrix[y][x]))
        minus_sum = sum(minus)
        if len(minus) % 2 == 0:
            return _sum - minus_sum
        return _sum + (-minus_sum + -abs_min * 2)
   

         