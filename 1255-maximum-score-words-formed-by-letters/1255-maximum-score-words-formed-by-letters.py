class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        def can_make_word(word):
            for key, cnt in Counter(word).items():
                if cache[key] < cnt:
                    return False
            return True
        
        def remove_cache(word):
            for key, cnt in Counter(word).items():
                cache[key] -= cnt
        
        def restore_cache(word):
            for key, cnt in Counter(word).items():
                cache[key] += cnt
        
        def get_score(word):
            ret = 0
            for key, cnt in Counter(word).items():
                ret += score[ord(key) - ord("a")] * cnt
            return ret
        
        def recur(depth, score):
            nonlocal answer
            if depth >= len(words):
                answer = max(answer, score)
                return 
            
            word = words[depth]
            
            if not can_make_word(word):
                answer = max(answer, score)
                return
           
            for i in range(depth, len(words)):
                remove_cache(word)
                recur(i + 1, score + get_score(word))
                restore_cache(word)
         
                
                
        answer = 0
        cache = Counter(letters)
        visited = [0 for _ in range(len(words))]
        for i in range(len(words)):
            recur(i, 0)
        return answer