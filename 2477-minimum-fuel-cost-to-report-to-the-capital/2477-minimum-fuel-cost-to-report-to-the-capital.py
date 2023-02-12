import math

class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        def dfs(node):
            nonlocal answer
            
            p = 1

            for child in graph[node]:
                if visited[child]:
                    continue
                visited[child] = 1
                person, car = dfs(child)
                p += person
                answer += car
                
            return p, math.ceil(p / seats)
                
        n = len(roads) + 1
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        answer = 0
        
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        visited[0] = 1 
        dfs(0)
        
        return answer
    
    
        
        
        