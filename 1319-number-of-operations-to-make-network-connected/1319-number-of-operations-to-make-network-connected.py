from collections import deque

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        p = [i for i in range(n)]
        count = 1
        for u, v in connections:
            if find(u) == find(v):
                continue
            else:  
                count += 1
                union(u, v)
                
        return n - count