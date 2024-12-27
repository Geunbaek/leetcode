class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        max_so_far = values[0]
        max_score = 0
        
        for j in range(1, n):
            curr_score = max_so_far + values[j] - j
            max_score = max(max_score, curr_score)
            
            max_so_far = max(max_so_far, values[j] + j)
        
        return max_score