class Solution:
    def longestPalindrome(self, s: str) -> int:
        cache = defaultdict(int)
        
        for char in s:
            cache[char] += 1
            
        answer = 0
        odd_count = 0
        for key, cnt in cache.items():
            answer += cnt // 2
            odd_count += cnt % 2
            
        if odd_count:
            return answer * 2 + 1
        return answer * 2
        