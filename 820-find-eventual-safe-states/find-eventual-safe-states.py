class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        degree = [0 for _ in range(n)]
        rev_graph = [[] for _ in range(n)]
        answer = []
        
        for i in range(n):
            for node in graph[i]:
                degree[i] += 1
                rev_graph[node].append(i)
                
        q = deque()
        
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
                    
        while q:
            now = q.popleft()
            answer.append(now)
            for _next in rev_graph[now]:
                degree[_next] -= 1
                if degree[_next] == 0:
                    q.append(_next)
                
        return sorted(answer)
            