import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        alpha = defaultdict(int)
        h = []
        
        for char in s:
            alpha[char] += 1
            
        for key, val in alpha.items():
            heapq.heappush(h, (-val, key))
            
        answer = []
        
        while h:
            count, c = heapq.heappop(h)
            
            if answer and answer[-1] == c:
                if not h:
                    return ""
                count2, c2 = heapq.heappop(h)
                answer.append(c2)
                heapq.heappush(h, (count, c))  
                if -count2 > 1:
                    heapq.heappush(h, (count2 + 1, c2))
                continue

            answer.append(c)
            
            if -count > 1:
                heapq.heappush(h, (count + 1, c))
                
        return "".join(answer)
            
            
        
        