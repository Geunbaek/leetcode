from collections import defaultdict, deque

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        n = len(ring)
        kn = len(key)
        cache = defaultdict(set)
        visited = set()
        for i, c in enumerate(ring):
            cache[c].add(i)
        
        q = []
        q.append((0, 0, 0))
        while q:
            cnt, depth, now = heapq.heappop(q)
            if depth == kn:
                return cnt
            if (depth, now) in visited:
                continue
                
            visited.add((depth, now))
            
            for i in cache[key[depth]]:
                clockwise = abs(i - now)
                anticlockwise = n - clockwise
                diff = min(clockwise, anticlockwise)
                heapq.heappush(q, (cnt + diff + 1, depth + 1, i))
        return -1
            