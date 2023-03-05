from collections import defaultdict, deque

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def bfs():
            q = deque([(0, 0)])
            visited = [0 for _ in range(len(arr))]
            visited[0] = 1
            
            while q:
                now, count = q.popleft()
                if now == len(arr) - 1:
                    return count
                el = arr[now]
                
                for i in (-1, 1):
                    _next = now + i
                    if not (0 <= _next < len(arr)):
                        continue
                        
                    if visited[_next] == 1:
                        continue
                        
                    visited[_next] = 1
                    q.append((_next, count + 1))
                
        
                for _next in cache[el]:
                    if _next == now:
                        continue
                        
                    if visited[_next] == 1:
                        continue
                        
                    visited[_next] = 1
                    q.append((_next, count + 1))
              
               
                cache[el].clear()
                    
            return -1          
        
        cache = defaultdict(set)
        
        for i in range(len(arr)):
            cache[arr[i]].add(i)
      
        return bfs()
            
        