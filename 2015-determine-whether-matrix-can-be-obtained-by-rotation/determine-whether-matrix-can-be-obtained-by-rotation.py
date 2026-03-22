class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def is_equal(mat1, mat2):
            r1, c1 = len(mat1), len(mat1[0])
            r2, c2 = len(mat2), len(mat2[0])

            if r1 != r2 or c1 != c2:
                return False
            
            for y in range(r1):
                for x in range(c1):
                    if mat1[y][x] != mat2[y][x]:
                        return False
            return True
        
        def rotate_90deg(mat):
            r, c = len(mat), len(mat[0])
            ret = [[0 for y in range(c)] for x in range(r)]

            for y in range(r):
                for x in range(c):
                    ret[x][-(y + 1)] = mat[y][x]

            return ret
    
        for i in range(4):
            if i == 0:
                if is_equal(mat, target):
                    return True
                continue
            mat = rotate_90deg(mat)
            if is_equal(mat, target):
                return True
        return False
            
