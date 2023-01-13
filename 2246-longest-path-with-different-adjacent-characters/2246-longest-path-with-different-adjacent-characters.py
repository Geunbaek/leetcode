
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def dfs(node):
            counter = []
            for child in graph[node]:
                l, alpha = dfs(child)
                if alpha == s[node]:
                    continue
                counter.append(l)
                
            if not counter:
                ls.append(1)
                return 1, s[node]
            
            counter.sort()
            if len(counter) == 1:
                ls.append(counter[-1] + 1)
                return counter[-1] + 1, s[node]
            else:
                ls.append((counter[-1] + counter[-2] + 1))
                return counter[-1] + 1, s[node]
                
          
    
        graph= [[] for _ in range(len(parent))]
        ls = []
        
        for i in range(len(parent)):
            if parent[i] == -1:
                continue
            graph[parent[i]].append(i)
        dfs(parent.index(-1))
        
        return max(ls)
    
        