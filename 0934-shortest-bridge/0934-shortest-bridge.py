from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        seen = set()
        
        def bfs(x,y,label):
            q = deque([(x,y)])
            seen.add((x,y))
            grid[x][y] = label
            while q:
                x,y = q.popleft()
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y - 1),(x,y + 1)]:
                    if not (0 <= nx < n and 0 <= ny < m ) :continue 
                    if (nx,ny) in seen:continue 
                    if grid[nx][ny] == 0 :continue
                    seen.add((nx,ny))
                    q.append((nx,ny))
                    grid[nx][ny] = label
        label = 2
        for i in range(n):
            for j in  range(m):
                if (i,j) in seen or grid[i][j] == 0:continue
                bfs(i,j,label)
                label += 1
        # 한쪽에서 bfs 를 돌려 
        def bfs_1():
            q = deque([])
            vis = set()
            for i in range(n):
                for j in range(m):
                    # 2를기준으로 넣기 
                    if grid[i][j] == 2:
                        q.append((i,j,0))
                        vis.add((i,j))
            res = int(1e10)
            while q:
                x,y,dist = q.popleft()
                for nx,ny in [(x + 1,y),(x - 1,y),(x,y + 1),(x,y - 1)]:
                    if not (0 <= nx < n and 0 <= ny < m):continue 
                    if (nx,ny) in vis:continue 
                    # 3이면 연결된거니 답 갱신 
                    if grid[nx][ny] == 3:
                        res = min(res,dist)
                    # 2라면 필요없고 
                    elif grid[nx][ny] == 2:
                        continue
                    # 0이라면 
                    else:
                        q.append((nx,ny,dist + 1))
                        vis.add((nx,ny))
            return res
        return bfs_1()