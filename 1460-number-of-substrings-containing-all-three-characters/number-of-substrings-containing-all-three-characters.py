class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        cache = defaultdict(int)
        answer = 0

        left = 0
        right = 0
        while right < n:
            cache[s[right]] += 1
            while len(cache) == 3:
                answer += n - right
                cache[s[left]] -= 1
                if cache[s[left]] == 0:
                    del cache[s[left]]
                left += 1
            right += 1

        return answer
