class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp
            
        def check(parent):
            q = deque([parent])
            visited = set([parent])
            
            while q:
                now = q.popleft()

                if len(graph[now]) != cache[parent] - 1:
                    return False

                for _next in graph[now]:
                    if _next in visited:
                        continue
                    
                    visited.add(_next)
                    q.append(_next)

            return True


        p = [i for i in range(n)]
        graph = [[] for _ in range(n)]
        for u, v in edges:
            union(u, v)
            graph[u].append(v)
            graph[v].append(u)
        
        cache = defaultdict(int)

        for i in range(n):
            cache[find(i)] += 1

        answer = 0
        for key, value in cache.items():
            if check(key):
                answer += 1
        return answer

    