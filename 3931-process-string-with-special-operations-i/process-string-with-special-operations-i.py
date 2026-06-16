class Solution:
    def processStr(self, s: str) -> str:
        answer = ""

        for c in s:
            if c.islower():
                answer += c
            elif c == '*':
                answer = answer[:-1]
            elif c == "#":
                answer += answer
            elif c == '%':
                answer = answer[::-1]
        return answer