class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        answer = 0
        mask = 0
        left = 0

        for right in range(n):
            while mask & nums[right] != 0:
                mask ^= nums[left]
                left += 1
            mask |= nums[right]
            answer = max(answer, right - left + 1)
        return answer
