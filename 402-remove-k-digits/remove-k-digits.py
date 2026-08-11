class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        n = len(num)
        if n == k:
            return "0"

        stack = deque()

        for c in num:
            while stack and stack[-1] > c and k:
                stack.pop()
                k -= 1
            stack.append(c)

        while k:
            stack.pop()
            k -= 1
        
        while stack and stack[0] == '0':
            stack.popleft()

        if not stack:
            return "0"
        return "".join(stack)
        