class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        n = len(words)
        
        flat_word = "".join(words)
        
        for word, cnt in Counter(flat_word).items():
            if not cnt % n == 0:
                return False
            
        return True
            
        