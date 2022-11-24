from collections import deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bfs(x, y):
            q = [(x, y, 1, set([(x, y)]))]
            
            while q:
                now_x, now_y, index, path = q.pop()
            
                if index >= len(word):
                    return True
               
                for i in range(4):
                    nx = now_x + dx[i]
                    ny = now_y + dy[i]
                    if not (0 <= nx < c and 0 <= ny < r):
                        continue
                    if (nx, ny) not in path and board[ny][nx] == word[index]:
                        q.append((nx, ny, index + 1, path | set([(nx, ny)])))
            return False
        
        r, c = len(board), len(board[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        
        for y in range(r):
            for x in range(c):
                if board[y][x] == word[0] and bfs(x, y):
                    return True
        return False