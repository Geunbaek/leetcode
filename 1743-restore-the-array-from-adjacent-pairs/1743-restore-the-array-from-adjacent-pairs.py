class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs) + 1
    
        graph = defaultdict(list)
        degree = defaultdict(int)
        visited = defaultdict(int)
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
            degree[u] += 1
            degree[v] += 1
            
        q = deque()
        for i in graph.keys():
            if degree[i] == 1:
                q.append(i)
                visited[i] = 1
                break
     
        answer = []
        
        while q:
            now = q.popleft()
            answer.append(now)
            for _next in graph[now]:
                if visited[_next] == 1:
                    continue
                visited[_next] = 1
                q.append(_next)
                
        return answer
        