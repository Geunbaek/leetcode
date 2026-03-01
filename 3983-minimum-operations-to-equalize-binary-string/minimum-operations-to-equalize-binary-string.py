from collections import deque

class Solution:
    def minOperations(self, s: str, k: int) -> int:
        n = len(s)
        no = s.count('1')
        
        if no == n:
            return 0
            
        parent = list(range(n + 3))
        
        def find(i):
            while i != parent[i]:
                parent[i] = parent[parent[i]]
                i = parent[i]
            return i
        q = deque([(no, 0)]) 
        
        parent[no] = find(no + 2)
        
        while q:
            curr_ones, cnt = q.popleft()
            
            min_i = max(0, k - curr_ones)
            max_i = min(n - curr_ones, k)
            
            L = curr_ones + 2 * min_i - k
            R = curr_ones + 2 * max_i - k
            
            nxt = find(L)
            while nxt <= R:
                if nxt == n: # 목표 도달
                    return cnt + 1
                
                q.append((nxt, cnt + 1))
                
                parent[nxt] = find(nxt + 2)
                
                nxt = find(nxt) 
                
        return -1