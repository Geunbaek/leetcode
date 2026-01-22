class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted(nums):
            return sorted(nums) == nums
        count = 0
        while not is_sorted(nums):
            _sums = []

            for i in range(len(nums) - 1):
                heapq.heappush(_sums, (nums[i] + nums[i + 1], i))

            _sum, i = heapq.heappop(_sums)
            nums[i] = _sum
            nums.pop(i + 1)
            count += 1
        return count