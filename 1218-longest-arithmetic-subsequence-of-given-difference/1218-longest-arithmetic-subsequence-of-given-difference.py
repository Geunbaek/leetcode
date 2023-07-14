from collections import defaultdict

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        cache = defaultdict(int)
        answer = 0
        
        for num in arr:
            if num - difference in cache:
                cache[num] = cache[num - difference] + 1
            else:
                cache[num] = 1
            answer = max(answer, cache[num])
                
        return answer
        