class Solution:
    def check(self, board, nx, ny, img1):
        count = 0
        
        for y in range(ny, ny + len(img1)):
            for x in range(nx, nx + len(img1)):
                if board[y][x] == 1 and img1[y - ny][x - nx] == 1:
                    count += 1
        return count
    
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        answer = 0
        board = [[0 for _ in range(90)] for _ in range(90)]
        
        for y in range(len(img2)):
            for x in range(len(img2[y])):
                board[30 + y][30 + x] = img2[y][x]

                
        for y in range(30 - len(img1), 30 + len(img1)):
            for x in range(30 - len(img1), 30 + len(img1)):
                answer = max(answer, self.check(board, x, y, img1))
                
        return answer
                