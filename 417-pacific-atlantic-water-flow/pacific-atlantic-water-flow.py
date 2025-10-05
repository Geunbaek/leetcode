class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def bfs(sx, sy):
            q = deque([(sx, sy)])

            visited = set([(sx, sy)])
            can_flow_pacific = False
            can_flow_atlantic = False

            while q:
                x, y = q.popleft()

                if can_flow_atlantic and can_flow_pacific:
                    break

                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    if nx < 0 or ny < 0:
                        can_flow_pacific = True
                        continue

                    if nx >= c or ny >= r:
                        can_flow_atlantic = True
                        continue
                  
                    if (nx, ny) in visited:
                        continue

                    if heights[y][x] < heights[ny][nx]:
                        continue

                    visited.add((nx, ny))
                    q.append((nx, ny))
            return can_flow_pacific, can_flow_atlantic
                
        r, c = len(heights), len(heights[0])
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        answer = []
        for y in range(r):
            for x in range(c):
                can_flow_pacific, can_flow_atlantic = bfs(x, y)
                if can_flow_pacific and can_flow_atlantic:
                    answer.append([y, x])

        return answer