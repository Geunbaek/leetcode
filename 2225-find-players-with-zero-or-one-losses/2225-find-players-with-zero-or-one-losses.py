class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        cache = defaultdict(int)
        
        for w, l in matches:
            if w not in cache:
                cache[w] = 0
            cache[l] += 1
            
        answer = [[], []]
        
        for key, val in cache.items():
            if val > 1:
                continue
            answer[val].append(key)
        
        for i in range(2):
            answer[i].sort()
        return answer
                
                
            
        