from collections import deque
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        
        board_map = {}
        
        for y in range(n-1, -1, -1):
            if (n - y - 1) % 2 != 0:
                line = [i for i in range((n - y - 1) * n + n, (n - y - 1) * n, -1)]
                for x in range(n):
                    board_map[line[x]] = (x, y)
            else:
                line = [i for i in range((n - y - 1) * n + 1, (n - y - 1) * n + n + 1)]
                for x in range(n):
                    board_map[line[x]] = (x, y)
    
        
        def bfs(start):
            q = deque([(start, 0)])
            visited = [0 for _ in range(n * n + 1)]
            visited[start] = 1
            
            while q:
                now, cnt = q.popleft()
                if now > n * n:
                    continue
                if now == n * n:
                    return cnt
    
                for i in range(1, 7):
                    _next = now + i
                    if _next > n * n:
                        continue
                    x, y = board_map[_next]
                    if board[y][x] == -1:
                        if visited[_next] == 1:
                            continue
                        visited[_next] = 1
                        q.append((_next, cnt + 1))
                    else:
                        _next = board[y][x]
                        if visited[_next] == 1:
                            continue
                        visited[_next] = 1
                        q.append((_next, cnt + 1))
            return -1
        return bfs(1)  
                    
                    
        
        