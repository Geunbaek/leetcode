class Solution:
    def clearStars(self, s: str) -> str:
        n = len(s)
        h = []

        for i, c in enumerate(s):
            if c == "*":
                if not h:
                    continue
                
                heappop(h)
                continue
            heappush(h, (c, -i))
        
        answer = ["" for _ in range(n)]

        while h:
            c, i = heappop(h)
            answer[-i] = c

        return ''.join(answer)