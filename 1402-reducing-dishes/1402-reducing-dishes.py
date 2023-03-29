class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        answer = 0
        n = len(s)
        for y in range(n):
            val = 0
            for x in range(n - y):
                val += s[y + x] * (x + 1)
            answer = max(answer, val)
            
        return answer
                
                
                
            
        
        