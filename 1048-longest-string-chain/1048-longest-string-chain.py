from collections import defaultdict

class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache = defaultdict(int)
        words.sort(key = len)
        
        for word in words:
            n = len(word)
            cache[word] = 1
            
            for i in range(n):
                w = word[:i] + word[i + 1:]
                
                if w in cache:
                    cache[word] = max(cache[w] + 1, cache[word])
                    
        return max(cache.values())
        
      