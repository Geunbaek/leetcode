class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        def is_concatenated(word, count):
            if not word and count >= 2:
                return True
            
            subword = ""
            for i, char in enumerate(word):
                subword += char # append char to the end of the subword
                if subword in words_set:
                    if is_concatenated(word[i + 1:], count + 1):
                        return True
                    
        words_set = set()
        
        for word in words:
            words_set.add(word)
        
        res = []
        for word in words:
            if is_concatenated(word, 0):
                res.append(word)
            
        return res
        