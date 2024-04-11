import sys
sys.set_int_max_str_digits(1000000000) 

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for c in num:
            c = int(c)
            while k and stack and int(stack[-1]) > c:
                stack.pop()
                k -= 1
            stack.append(str(c))
        
        while k:
            stack.pop()
            k -= 1
        
        if not stack:
            return '0'
        answer = int("".join(stack))
        return str(answer)
            