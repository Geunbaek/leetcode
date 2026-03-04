class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def is_special(x, y):
            for ny in range(r):
                if y == ny:
                    continue

                if mat[ny][x] == 1:
                    return False
        
            for nx in range(c):
                if x == nx:
                    continue
                
                if mat[y][nx] == 1:
                    return False
            return True

        r, c = len(mat), len(mat[0])
        answer = 0
        for y in range(r):
            for x in range(c):
                if mat[y][x] == 1 and is_special(x, y):
                    answer += 1
        return answer 