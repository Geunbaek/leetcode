class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        r = len(mat)
        c = len(mat[0])
        
        def check(x, y, d):
            while True:
                nx = x + dx[d]
                ny = y + dy[d]
                if not (0 <= nx < c and 0 <= ny < r):
                    return True
                
                if mat[ny][nx] == 1:
                    return False
                x = nx
                y = ny            
        ans = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        for y in range(r):
            for x in range(c):
                if mat[y][x] != 1:
                    continue
                for i in range(4):
                    if not check(x, y, i):
                        break
                else:
                    ans += 1
        return ans