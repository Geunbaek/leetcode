class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        _max = 0
        for left in range(n):
            even = defaultdict(int)
            odd = defaultdict(int)
            max_len = 0
            for right in range(left, n):
                if nums[right] % 2 == 0:
                    even[nums[right]] += 1
                else:
                    odd[nums[right]] += 1
                if len(even) == len(odd):
                    max_len = right - left + 1
            _max = max(_max, max_len)

        return _max