class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        def find(x):
            if x != p[x]:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            if ap > bp:
                p[ap] = bp
            else:
                p[bp] = ap

        cache = defaultdict(list)
        off_cache = defaultdict(set)
        p = [i for i in range(c + 1)]
        answer = []

        for u, v in connections:
            if find(u) != find(v):
                union(u, v)

        for i in range(1, c + 1):
            heappush(cache[find(i)], i)
        for q, node in queries:
            parent = find(node)
            if q == 1:
                if node not in off_cache[parent]:
                    answer.append(node)
                    continue
                while cache[parent] and cache[parent][0] in off_cache[parent]:
                    heappop(cache[parent])
                if cache[parent]:
                    answer.append(cache[parent][0])
                else:
                    answer.append(-1)
            if q == 2:
                off_cache[parent].add(node)
        return answer