class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        def find(p, x):
            if x != p[x]:
                p[x] = find(p, p[x])
            return p[x]
        
        def union(p, a, b):
            ap = find(p, a)
            bp = find(p, b)
            
            p[ap] = bp
            
        
        total = 0
        for i in range(len(edges)):
            edges[i].append(i)
            
        edges.sort(key = lambda x: x[2])
        p = [i for i in range(n)]
        
        for u, v, c, j in edges:
            if find(p, u) != find(p, v):
                union(p, u, v)
                total += c
   
        a = set()
        b = set()
        for u1, v1, c1, i in edges:
            temp = 0
            temp_p = [i for i in range(n)]

            for u, v, c, j in edges:
                if i == j :
                    continue
                if find(temp_p, u) != find(temp_p, v):
                    union(temp_p, u, v)
                    temp += c

            mesh = set()
            for k in range(n):
                mesh.add(find(temp_p, k))
            
            if len(mesh) != 1 or temp > total:
                a.add(i)

            if i in a:
                continue
                    
            temp = 0
            temp_p = [i for i in range(n)]
            union(temp_p, u1, v1)
            temp += c1
            
            for u, v, c, j in edges:
                if i == j :
                    continue
                if find(temp_p, u) != find(temp_p, v):
                    union(temp_p, u, v)
                    temp += c
                    
            mesh = set()
            for k in range(n):
                mesh.add(find(temp_p, k))
                
            if len(mesh) == 1 and temp == total:
                b.add(i)
            
        return [a, b]
                        
        