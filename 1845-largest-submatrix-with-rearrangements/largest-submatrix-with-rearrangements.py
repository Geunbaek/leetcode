class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        r = len(matrix)
        c = len(matrix[0])
        ans = 0

        for y in range(r):
            for x in range(c):
                if matrix[y][x] != 0 and y > 0:
                    matrix[y][x] += matrix[y - 1][x]

            curr_row = sorted(matrix[y], reverse=True)
            for i in range(c):
                ans = max(ans, curr_row[i] * (i + 1))

        return ans