from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = defaultdict(int)
        answer = 0
        _sum = 0
        result[0] = 1
    
        for num in nums:
            _sum = (_sum + num % k + k) % k
            answer += result[_sum]
            result[_sum] += 1
            
        return answer
            
        