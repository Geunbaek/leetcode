class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        cache = defaultdict(list)
        answer = -1
        for i, char in enumerate(s):
            if char in cache:
                answer = max(answer, i - cache[char][0] - 1)
            cache[char].append(i)
            
        return answer
            
        