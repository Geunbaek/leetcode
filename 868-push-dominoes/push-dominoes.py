class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        
        q = deque()
        dominoes = list(dominoes)
        for i, domino in enumerate(dominoes):
            if domino == ".":
                continue
            q.append((i, domino))

        dx = {"R": 1, "L": -1}
        while q:
            length = len(q)
            cache = {}

            while length:
                x, domino = q.popleft()
                length -= 1
                nx = x + dx[domino]
                if not (0 <= nx < n):
                    continue

                if dominoes[nx] != ".":
                    continue
                    
                if nx in cache:
                    del cache[nx]
                    continue

                cache[nx] = domino

            for key, value in cache.items():
                dominoes[key] = value
                q.append((key, value))

        return "".join(dominoes)

