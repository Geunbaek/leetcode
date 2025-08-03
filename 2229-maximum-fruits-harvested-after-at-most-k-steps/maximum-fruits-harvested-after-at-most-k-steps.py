from typing import List

class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:
        MAX = 2 * 10**5 + 10
        fruit_amounts = [0] * MAX
        for pos, amt in fruits:
            fruit_amounts[pos] = amt

        # prefix[i] = sum of fruits from 0 to i-1
        prefix = [0] * (MAX + 1)
        for i in range(1, MAX + 1):
            prefix[i] = prefix[i - 1] + fruit_amounts[i - 1]

        def get_sum(l, r):
            return prefix[r + 1] - prefix[l]

        answer = 0

        # Try all possible l from 0 to startPos, and find max r such that condition holds
        for l in range(max(0, startPos - k), startPos + 1):
            # r must satisfy: min(startPos - l, r - startPos) + (r - l) <= k
            # Since we're going left first, then right: total cost = (startPos - l) + (r - startPos) = r - l
            # But if we turn at l, total cost = (startPos - l) * 2 + (r - startPos)
            # The tighter formula is:
            max_r = min(MAX - 1, max(startPos, k - 2 * (startPos - l) + startPos))
            if max_r < l:
                continue
            answer = max(answer, get_sum(l, max_r))

        # Try all possible r from startPos to MAX, and find min l such that condition holds
        for r in range(startPos, min(MAX, startPos + k + 1)):
            # go right first, then left
            max_l = max(0, min(startPos, startPos - (k - 2 * (r - startPos))))
            if max_l > r:
                continue
            answer = max(answer, get_sum(max_l, r))

        return answer
