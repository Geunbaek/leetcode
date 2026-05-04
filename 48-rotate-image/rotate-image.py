class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        # Transpose
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for k in range(n):
            i, j = 0, n - 1
            while i < j:   
                matrix[k][i], matrix[k][j] = matrix[k][j], matrix[k][i]
                i += 1
                j -= 1