class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        l, r = 0, n * m - 1

        while l <= r:
            mid = (l + r) // 2
            x, y = mid % m, mid // m

            if matrix[y][x] > target:
                r = mid - 1
            else:
                l = mid + 1
        tx, ty = r % m, r // m

        return matrix[ty][tx] == target 