class Solution:
    def maxDepth(self, s: str) -> int:
        answer = 0
        depth = 0
        for c in s:
            if c == "(":
                depth += 1
            elif c == ")":
                answer = max(answer, depth)
                depth -= 1
        return answer            