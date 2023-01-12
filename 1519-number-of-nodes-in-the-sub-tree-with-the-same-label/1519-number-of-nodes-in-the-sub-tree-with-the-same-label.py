class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
            
        graph = [[] for _ in range(n)]
        visited = [0 for _ in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
            
        counts = [0] * len(string.ascii_lowercase)
        answer = [0] * n
        
        def dfs(node, parent):
            index = ord(labels[node]) - ord('a')
            previous = counts[index]
            counts[index] += 1
            
            for child in graph[node]:
                if child != parent:
                    dfs(child, node)
                    
            answer[node] = counts[index] - previous
        
        dfs(0, -1)
        return answer