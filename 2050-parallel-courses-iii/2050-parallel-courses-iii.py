from collections import deque

class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        dist = [0 for _ in range(n + 1)]
        time = [0] + time
        q = deque()
        
        graph = [[] for _ in range(n + 1)]
        degree = [0 for _ in range(n + 1)]
        
        for prev, next in relations:
            graph[prev].append(next)
            degree[next] += 1
            
        for i in range(1, n + 1):
            if degree[i] == 0:
                dist[i] = time[i]
                q.append((i, time[i]))
     
        while q:
            now, t = q.popleft()
            for next in graph[now]:
                degree[next] -= 1
                dist[next] = max(dist[next], time[next] + max(dist[now], t))
                if degree[next] == 0:
                    q.append((next, t + time[next]))
       
        return max(dist)