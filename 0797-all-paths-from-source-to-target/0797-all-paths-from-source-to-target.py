class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        visited = [0 for _ in range(len(graph))]
        answer =[]
        
        def dfs(node, path):
            flag = False
            if path[-1] == len(graph) - 1:
                answer.append(path)
                return 
            
            for _next in graph[node]:
                if visited[_next] == 0:
                    visited[_next] = 1
                    dfs(_next, path + [_next])
                    visited[_next] = 0
                    flag = True
                    
                    
        visited[0] = 1
        dfs(0, [0])
            
        return answer