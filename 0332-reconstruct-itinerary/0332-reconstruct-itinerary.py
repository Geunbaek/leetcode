from collections import defaultdict

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)
        
        for i, (u, v) in enumerate(tickets):
            graph[u].append((v, i))
            
        for key in graph.keys():
            graph[key].sort()
            
        
        n = len(tickets)
        visited = [0 for _ in range(n)]
        answer = []
        
        def recur(depth, path):
            if depth >= n:
                answer.append(path)
                return
            
            if answer:
                return
            
            prev = path[-1]
            for _next, ti in graph[prev]:
                if visited[ti] == 1:
                    continue
                visited[ti] = 1
                recur(depth + 1, path + [_next])
                visited[ti] = 0
        
        recur(0, ["JFK"])
        return answer[0]
                
        
        
    
        