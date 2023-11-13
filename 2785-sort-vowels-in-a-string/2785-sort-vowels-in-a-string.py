class Solution:
    def sortVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        v = []
        
        for char in s:
            if char in vowels:
                v.append(char)
        
        v.sort(reverse=True)
        
        answer = []
        
        for char in s:
            if char in vowels:
                answer.append(v.pop())
            else:
                answer.append(char)
        return "".join(answer)
        