class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        _min = 1_000_000_000
        _max = 0

        for num in nums:
            _min = min(_min, num)
            _max = max(_max, num)
        return (_max - _min) * k