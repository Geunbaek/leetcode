class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        result = []

        for c in s:
            if c == "(":
                stack.append(len(result))
            elif c == ")":
                start = stack.pop()
                result[start:] = result[start:][::-1]
            else:
                result.append(c)
        return "".join(result)