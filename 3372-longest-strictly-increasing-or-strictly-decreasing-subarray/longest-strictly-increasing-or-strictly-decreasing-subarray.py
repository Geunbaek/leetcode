class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        inc = 1
        desc = 1
        _max = 1

        for i in range(1, n):
            now = nums[i - 1]
            _next = nums[i]
            if now > _next:
                inc += 1
                desc = 1
            elif now < _next:
                desc += 1
                inc = 1
            else:
                inc = 1
                desc = 1
            _max = max(_max, inc, desc)
        return _max