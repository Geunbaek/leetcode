from collections import deque, defaultdict

class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        q = deque(arr)
        
        win_count = defaultdict(int)
        _max = max(arr)
        
        for _ in range(n - 1):
            first = q.popleft()
            second = q.popleft()
            win = first if first > second else second
            lose = second if first > second else first
            
            win_count[win] += 1
            q.appendleft(win)
            q.append(lose)
            
            if win_count[win] == k:
                return win
            
        return _max
           
        
                
            
        