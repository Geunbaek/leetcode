class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        counter = Counter(word)

        answer = len(word)
        for c1 in counter.values():
            deleted = 0
            for c2 in counter.values():
                if c1 > c2:
                    deleted += c2
                elif c2 > c1 + k:
                    deleted += c2 - (c1 + k)
            answer = min(answer, deleted)
        
        return answer