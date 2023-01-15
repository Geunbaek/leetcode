from collections import defaultdict

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
                
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        graph = [[] for _ in range(len(vals))]
        val_node_map = defaultdict(set)
        p = [i for i in range(len(vals))]
        answer = len(vals)
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
            val_node_map[vals[u]].add(u)
            val_node_map[vals[v]].add(v)
            
        for val in sorted(val_node_map.keys()):
            for node in val_node_map[val]:
                for _next in graph[node]:
                    if vals[_next] <= val:
                        union(node, _next)
                    
            count = defaultdict(int)
            for node in val_node_map[val]:
                count[find(node)] += 1
            
            for node in count.keys():
                answer += count[node] * (count[node] - 1) // 2
        return answer
        