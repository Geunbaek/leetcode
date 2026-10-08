class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        answer = []

        start = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(c)
                continue
            stack.pop()
            if not stack:
                answer.append(s[start + 1: i])
                start = i + 1
        return "".join(answer)
