class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c1 = Counter(chars)
        answer = 0
        for word in words:
            c2 = Counter(word)
            for char, cnt in c2.items():
                if char not in c1:
                    break
                if cnt > c1[char]:
                    break
            else:
                answer += len(word)
                
        return answer