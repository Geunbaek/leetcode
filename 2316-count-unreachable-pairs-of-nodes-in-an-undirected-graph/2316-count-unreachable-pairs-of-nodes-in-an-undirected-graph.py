from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        def get_score(n):
            ret = 0
            for i in range(n):
                ret += i
            return ret
        
        if len(edges) == 0:
            return get_score(n)
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            
            p[bp] = ap
            
        p = [i for i in range(n)]
        
        for u, v in edges:
            if find(u) != find(v):
                union(u, v)
        
        areas = defaultdict(int)

        
        for i in range(n):
            areas[find(i)] += 1
        
        answer = get_score(n)
        for i in areas.values():
            answer -= get_score(i)
          
      
        return answer
            
        
    