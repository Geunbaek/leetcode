class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def oper(word):
            stack = []
            for char in word:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return "".join(stack)
        
        return oper(s) == oper(t)
     
        