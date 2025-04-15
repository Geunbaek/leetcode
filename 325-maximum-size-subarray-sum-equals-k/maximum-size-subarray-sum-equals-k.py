class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefix_sum = [0]
        cache = {}
        answer = 0

        for i, num in enumerate(nums):
            _sum = prefix_sum[-1] + num
            prefix_sum.append(_sum)

            if _sum == k:
                answer = i + 1

            if _sum - k in cache:
                answer = max(answer, i - cache[_sum - k])

            if _sum not in cache:
                cache[_sum] = i
        return answer
        