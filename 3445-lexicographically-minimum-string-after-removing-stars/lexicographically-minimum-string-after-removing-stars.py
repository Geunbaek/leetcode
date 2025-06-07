class Solution:
    def clearStars(self, s: str) -> str:
        h = []
        cache = {}

        for i, c in enumerate(s):
            if c == "*":
                if not h:
                    continue
                
                _min, index = heappop(h)
                cache[_min].remove(-index)
                continue

            if c not in cache:
                cache[c] = set()

            heappush(h, (c, -i))
            cache[c].add(i)
        answer = ""

        for i, c in enumerate(s):
            if c == '*': continue
            if i in cache[c]:
                answer += c
        return answer