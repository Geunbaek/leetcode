class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        n = len(s)

        answer = 0
        left = 0

        while left < n:
            right = left

            while right < n and s[right] == s[left]:
                right += 1

            mid = right

            while right < n and s[right] == s[mid]:
                right += 1
            
            answer += min(mid - left, right - mid)
            left = mid
        return answer