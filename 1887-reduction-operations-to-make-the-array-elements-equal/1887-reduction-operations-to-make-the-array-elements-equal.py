class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n_h = set()
        n_cache = defaultdict(int)
        
        for i, num in enumerate(nums):
            n_h.add(num)
            n_cache[num] += 1
            
        if len(n_h) == 1:
            return 0
            
        n_h = sorted(n_h, reverse=True)
        answer = 0
        
        for i in range(len(n_h) - 1):
            _max = n_h[i]
            next_max = n_h[i + 1]
            n_cache[next_max] += n_cache[_max]
            answer += n_cache[_max]
    
        return answer
                
            
            
            
            
            
        