class Solution:
    def maxScore(self, s: str) -> int:
        n = len(s)
        score = 0
        
        for i in range(1, n):
            left = s[:i]
            right = s[i:]
     
            score = max(score, left.count("0") + right.count("1"))
             
        return score
        