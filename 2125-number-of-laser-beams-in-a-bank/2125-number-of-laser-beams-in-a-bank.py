class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        n = len(bank)
        
        q = deque()
        
        for i in range(n):
            now = bank[i].count('1')
            if now == 0:
                continue
            q.append(now)
            
        if not q:
            return 0
        
        while len(q) > 1:
            now = q.popleft()
            ans += now * q[0]
            
        return ans