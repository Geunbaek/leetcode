class Solution:
    def countAndSay(self, n: int) -> str:   
        def compress(s):
            stack = []

            for c in s:
                if not stack:
                    stack.append((1, c))
                    continue

                last_count, last_char = stack[-1]
                if last_char != c:
                    stack.append((1, c))
                else:
                    stack.pop()
                    stack.append((last_count + 1, c))
            return "".join(map(lambda x: "".join(map(str, x)), stack))

        dp = ["1"]

        for i in range(1, n):
            dp.append(compress(dp[i - 1]))
        return dp[n - 1]