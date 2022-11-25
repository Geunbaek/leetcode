class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [-1]
        ans = 0
        arr.append(-1)
        for i, n in enumerate(arr):
            while len(stack) > 1 and n <= arr[stack[-1]]:
                cur = stack.pop()
                ans += arr[cur] * (cur - stack[-1]) * (i - cur)

            stack.append(i)
            ans %= 1_000_000_007
        return ans