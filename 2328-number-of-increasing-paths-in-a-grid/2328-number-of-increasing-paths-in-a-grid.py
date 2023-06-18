class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        r,c=len(grid),len(grid[0])
        dp=[[0 for _ in range(c)] for _ in range(r)]
        dx=[-1,0,1,0]
        dy=[0,-1,0,1]
        mod=10**9+7
        
        def dfs(x,y):
            if dp[y][x]:
                return dp[y][x]
            ret = 1
            for i in range(4):
                nx=x+dx[i]
                ny=y+dy[i]
                if not (0<=nx<c and 0<=ny<r):
                    continue
                if grid[ny][nx] > grid[y][x]:
                    ret += dfs(nx,ny) 
            dp[y][x]=ret%mod
            return ret
        for y in range(r):
            for x in range(c):
                dfs(x,y)
        answer=0
        for y in range(r):
            for x in range(c):
                answer+=dp[y][x]
        return answer%mod
                    
            
            
        