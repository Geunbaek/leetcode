class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {
           "(": ")",
            "{": "}",
            "[": "]"
        }
        
        stack = []
        
        for char in s:
            if char in brackets:
                stack.append(char)
            else:
                if not stack:
                    return False
                elif brackets[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True