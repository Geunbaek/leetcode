class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        def dfs(x, y, px, py, depth, target):
            check.add((x, y))
            is_valid = False
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if not (0 <= nx < c and 0 <= ny < r):
                    continue
                if grid[ny][nx] != target:
                    continue
                if (nx, ny) == (px, py):
                    continue
                if visited[ny][nx]:
                    if depth - visited[ny][nx] + 1 >= 4:
                        return True
                    continue
                visited[ny][nx] = depth + 1
                is_valid |= dfs(nx, ny, x, y, depth + 1, target)
            return is_valid
            
        r, c = len(grid), len(grid[0])
        visited = [[0 for _ in range(c)] for _ in range(r)]
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        check = set()
        for y in range(r):
            for x in range(c):
                if visited[y][x]:
                    continue
                if dfs(x, y, -1, -1, 1, grid[y][x]):
                    print(x, y)
                    return True
        return False