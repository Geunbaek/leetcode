class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(l, r):
            while l >= 0 and r <= n - 1 and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1
        
        n = len(s)
        answer = ""
        for i in range(n):
            l, r = extend(i, i + 1)
            answer = max(answer, s[l:r + 1], key=len)
            l, r = extend(i, i)
            answer = max(answer, s[l:r + 1], key=len)
        return answer
            
        