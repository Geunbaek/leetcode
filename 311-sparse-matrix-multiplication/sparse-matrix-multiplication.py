class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])

        new_mat = [[0 for _ in range(c2)] for _ in range(r1)]


        for y in range(r1):
            for x in range(c2):
                cell = 0
                for y2 in range(r2):
                    cell += mat1[y][y2] * mat2[y2][x]
            
                new_mat[y][x] = cell

        return new_mat
                    