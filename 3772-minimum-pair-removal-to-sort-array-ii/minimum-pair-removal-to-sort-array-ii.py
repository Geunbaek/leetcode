import heapq

class Solution:
    def minimumPairRemoval(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0
        
        left = list(range(-1, n - 1))
        right = list(range(1, n + 1))
        
        vals = list(nums)
        
        valid = [True] * n
        
        pq = []
        inv_count = 0  
        
        for i in range(n - 1):
            s = vals[i] + vals[i+1]
            heapq.heappush(pq, (s, i))
            if vals[i] > vals[i+1]:
                inv_count += 1
                
        ops = 0
        
        while inv_count > 0:
            if not pq:
                break
                
            s, i = heapq.heappop(pq)
            j = right[i]
            
            if not valid[i] or j >= n or not valid[j]:
                continue
            if vals[i] + vals[j] != s:
                continue
            
            if vals[i] > vals[j]:
                inv_count -= 1
            
            l = left[i]
            if l != -1:
                if vals[l] > vals[i]:
                    inv_count -= 1
            
            r = right[j]
            if r != n:
                if vals[j] > vals[r]:
                    inv_count -= 1
            
            new_val = vals[i] + vals[j]
            vals[i] = new_val   
            valid[j] = False   
            
            right[i] = r
            if r != n:
                left[r] = i
            
            if l != -1:
                if vals[l] > vals[i]:
                    inv_count += 1
                heapq.heappush(pq, (vals[l] + vals[i], l))
                
            if r != n:
                if vals[i] > vals[r]:
                    inv_count += 1
                heapq.heappush(pq, (vals[i] + vals[r], i))
                
            ops += 1
            
        return ops