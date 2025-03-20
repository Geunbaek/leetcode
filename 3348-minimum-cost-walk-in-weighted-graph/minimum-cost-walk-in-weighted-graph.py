class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x]) 
            return p[x]
        
        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[bp] = ap

        costs = dict()
        
        p = [i for i in range(n)]
        for u, v, c in edges:
            up = find(u)
            vp = find(v)

            if up != vp:
                union(u, v)
                if vp in costs:
                    c &= costs[vp]

                if up in costs:
                    costs[up] &= c
                else:
                    costs[up] = c
            else:
                if vp in costs:
                    c &= costs[vp]

                if up in costs:
                    costs[up] &= c
                else:
                    costs[up] = c
        print(costs)
        answer = []
        for a, b in query:
            ap = find(a)
            bp = find(b)
            print(ap, bp)
            if ap == bp:
                answer.append(costs[bp])
            else:
                answer.append(-1)
        return answer