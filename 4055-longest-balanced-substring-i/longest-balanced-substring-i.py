class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)

        def is_balanced(cache):
            now = 0
            for key, cnt in cache.items():
                if now == 0:
                    now = cnt
                elif now != cnt:
                    return False
            return True

        answer = 0
        for i in range(n):
            cache = defaultdict(int)
            for j in range(i, n):
                cache[s[j]] += 1
                if is_balanced(cache):
                    answer = max(answer, j - i + 1)
        return answer