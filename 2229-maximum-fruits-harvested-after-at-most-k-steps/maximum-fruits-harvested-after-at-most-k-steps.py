from bisect import bisect_left, bisect_right

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        n = len(fruits)
        positions = [p for p, _ in fruits]
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + fruits[i][1]

        def get_sum(l, r):
            li = bisect_left(positions, l)
            ri = bisect_right(positions, r)
            return prefix[ri] - prefix[li]

        ans = 0
        # Go left x then right (k - 2x)
        for x in range(k + 1):
            l = startPos - x
            r = startPos + max(0, k - 2 * x)
            ans = max(ans, get_sum(l, r))

        # Go right x then left (k - 2x)
        for x in range(k + 1):
            r = startPos + x
            l = startPos - max(0, k - 2 * x)
            ans = max(ans, get_sum(l, r))

        return ans
