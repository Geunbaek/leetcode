from collections import deque

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        p = [i for i in range(n)]
        answer = [0 for _ in range(len(queries))]
        
        new_queries = [(i, query) for i, query in enumerate(queries)]
        new_queries.sort(key = lambda x: x[-1][2])
        edgeList.sort(key = lambda x: -x[2])
        
        for i, (s, e, max_c) in new_queries:
            while edgeList and edgeList[-1][2] < max_c:
                u, v, c = edgeList.pop()
                union(u, v)
            answer[i] = True if find(s) == find(e) else False
        
        return answer
        
  
    