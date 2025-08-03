from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        MAX = 2 * 10**5 + 5
        fruit_amounts = [0] * MAX
        for pos, amt in fruits:
            fruit_amounts[pos] = amt

        prefix = [0] * (MAX + 1)
        for i in range(MAX):
            prefix[i + 1] = prefix[i] + fruit_amounts[i]

        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        ans = 0
        for l in range(max(0, startPos - k), startPos + 1):
            r = min(MAX - 1, l + (k - min(startPos - l, k)))
            ans = max(ans, get_sum(l, r))

        for r in range(startPos, min(MAX, startPos + k + 1)):
            l = max(0, r - (k - min(r - startPos, k)))
            ans = max(ans, get_sum(l, r))

        return ans
