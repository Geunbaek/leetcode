class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ancestors = defaultdict(set)
        graph = [[] for _ in range(n)]    
        degree = [0 for _ in range(n)]
        answer = [[] for _ in range(n)]
    
        for u, v in edges:
            degree[v] += 1
            graph[u].append(v)
            
        q = deque()
        
        for i in range(n):
            if degree[i] == 0:
                q.append(i)
                
        while q:
            now = q.popleft()

            for _next in graph[now]:
                degree[_next] -= 1
                ancestors[_next].add(now)
                ancestors[_next] |= ancestors[now]
                if degree[_next] == 0:
                    q.append(_next)
        
        for node, ancestor in ancestors.items():
            answer[node].extend(sorted(ancestor)) 
            

        return answer
                
            