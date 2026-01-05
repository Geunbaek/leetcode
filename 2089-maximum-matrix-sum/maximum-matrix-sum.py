class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        _sum = 0
        minus_sum = 0
        minus_count = 0
        r,c = len(matrix), len(matrix[0])
        abs_min = 100_000
        for y in range(r):
            for x in range(c):
                if matrix[y][x] >= 0:
                    _sum += matrix[y][x]
                else:
                    minus_sum += matrix[y][x]
                    minus_count += 1
                abs_min = min(abs_min, abs(matrix[y][x]))
        if minus_count % 2 == 0:
            return _sum - minus_sum
        return _sum + (-minus_sum + -abs_min * 2)
   

         