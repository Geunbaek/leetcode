class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        is_zero = True 
        _all = 0
        for num in nums:
            _all ^= num
            if _all > 0:
                is_zero = False

        if _all > 0:
            return n
        return n - 1 if not is_zero else 0