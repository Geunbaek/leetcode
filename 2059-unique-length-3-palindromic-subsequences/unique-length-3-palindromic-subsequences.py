class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters = set(s)
        answer = 0

        for letter in letters:
            left, right = s.index(letter), s.rindex(letter)

            cs = set()
            for i in range(left + 1, right):
                cs.add(s[i])

            answer += len(cs)

        return answer