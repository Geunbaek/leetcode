class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        palindrome = list(palindrome)
        alphabet = [chr(ord('a') + i) for i in range(26)]
        flag = False
        for char in alphabet:
            for i in range(len(palindrome)):
                if len(palindrome) % 2 != 0 and i == len(palindrome) // 2:
                    continue
                if palindrome[i] > char:
                    palindrome[i] = char
                    return "".join(palindrome)
        
        for char in alphabet:
            if palindrome[-1] != char:
                palindrome[-1] = char
                
                return "".join(palindrome)