class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        def find(x):
            if p[x] != x:
                p[x] = find(p[x])
            return p[x]

        def union(a, b):
            ap = find(a)
            bp = find(b)
            p[ap] = bp

        n = len(source)
        p = [i for i in range(n)]

        for u, v in allowedSwaps:
            union(u, v)

        cache = defaultdict(lambda: defaultdict(int))
        for i in range(n):
            ip = find(i)
            cache[ip][source[i]] += 1

        ans = 0
        for i in range(n):
            ip = find(i)
            if cache[ip][target[i]] > 0:
                cache[ip][target[i]] -= 1
            else:
                ans += 1
        return ans
                    
