class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(now):
            ret = 0
            flag = False
            for _next in graph[now]:
                if visited[_next] != 0:
                    continue
                visited[_next] = 1
                flag = True
                ret += dfs(_next)

            if not flag and hasApple[now]:
                return 1
            
            if ret == 0 and hasApple[now]:
                if now == 0:
                    return 0
                return 1
        
            if now == 0:
                return ret
        
            return ret + 1 if ret else 0
        
            
        graph = [[] for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [0 for _ in range(n)]
        visited[0] = 1
        return dfs(0) * 2