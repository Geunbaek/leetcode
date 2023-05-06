class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = set("aeiou")
        vowel_cnt = 0
        
        for i in range(k):
            if s[i] in vowel:
                vowel_cnt += 1
        answer = vowel_cnt
        
        for i in range(k, len(s)):
            if s[i - k] in vowel:
                vowel_cnt -= 1
            if s[i] in vowel:
                vowel_cnt += 1
            answer = max(answer, vowel_cnt)
        return answer
                
        
        