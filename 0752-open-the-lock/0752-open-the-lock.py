class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        q = deque()
        cache = set(deadends)
        
        if "0000" not in cache:
            cache.add("0000")
            q.append(("0000", 0))
            
        while q:
            now, count = q.popleft()
            if now == target:
                return count
            for i in range(4):
                _next = now[: i] + str((int(now[i]) + 1) % 10) + now[i + 1:]
                if _next not in cache:
                    cache.add(_next)
                    q.append((_next, count + 1))
                _next = now[: i] + str((int(now[i]) - 1) % 10) + now[i + 1:]
                if _next not in cache:
                    cache.add(_next)
                    q.append((_next, count + 1))
        return -1