class Solution:
    def smallestSubsequence(self, s: str) -> str:
        memo = Counter(s)
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
                memo[c] -= 1
                continue
            if c in stack:
                memo[c] -= 1
                continue
            while stack and stack[-1] > c and memo[stack[-1]] > 0:
                stack.pop()
            stack.append(c)
            memo[c] -= 1
        return "".join(stack)