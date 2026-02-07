class Solution:
    def minimumDeletions(self, s: str) -> int:
        stack = []
        answer = 0

        for c in s:
            if stack and stack[-1] == 'b' and c == 'a':
                stack.pop()
                answer += 1
            else:
                stack.append(c)
                
        return answer