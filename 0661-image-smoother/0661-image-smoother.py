class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        def sum(x, y):
            total = img[y][x]
            count = 1
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                total += img[ny][nx]
                count += 1
            return total, count
                
        
        dx = [0, 1, 1, 1, 0, -1, -1, -1]
        dy = [-1, -1, 0, 1, 1, 1, 0, -1]
        
        r, c = len(img), len(img[0])
        
        new = [[0 for _ in range(c)] for _ in range(r)]
        
        for y in range(r):
            for x in range(c):
                total, count = sum(x, y)
                new[y][x] = total // count
                
        return new
                
        