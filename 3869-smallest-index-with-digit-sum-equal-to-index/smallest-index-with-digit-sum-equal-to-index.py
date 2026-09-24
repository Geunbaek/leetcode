class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def i_sum(nums):
            return sum(map(lambda x: int(x), str(nums)))

        for i, num in enumerate(nums):
            if i_sum(num) == i:
                return i
        return -1