class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        
        for char in s:
            if stack and stack[-1] >= k:
                break
                
            if char.isalpha():
                if not stack:
                    stack.append(1)
                else:
                    stack.append(stack[-1] + 1)
            else:
                if not stack:
                    continue
                stack.append(stack[-1] * int(char))
        
        for i in range(len(stack) - 1, -1, -1):
            k %= stack[i]
            if k == 0 and s[i].isalpha():
                return s[i]
        