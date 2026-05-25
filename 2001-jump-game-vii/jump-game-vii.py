class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[n - 1] == '1':
            return False
            
        q = deque([0])
        max_reached = 0 
        
        while q:
            now = q.popleft()
            
            if now == n - 1:
                return True
                
            _min = now + minJump
            _max = min(now + maxJump, n - 1)
            
            start = max(_min, max_reached + 1)
            
            for next_idx in range(start, _max + 1):
                if s[next_idx] == '0':
                    q.append(next_idx)
            
            max_reached = max(max_reached, _max)

        return False
        