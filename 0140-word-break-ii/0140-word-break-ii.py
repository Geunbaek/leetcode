class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:    
        def recur(depth, now, path):
            if depth >= n:
                if not now:
                    answer.append(" ".join(path))
                if now in cache:
                    answer.append(" ".join(path + [now]))
                return;
            if now in cache:
                recur(depth + 1, s[depth], path + [now])
                recur(depth + 1, now + s[depth], path)
            else:
                recur(depth + 1, now + s[depth], path)
        
        n = len(s)
        answer = []
        cache = set()
        
        for word in wordDict:
            cache.add(word)
        
        recur(0, "", [])
        return answer            
        
        