class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_possible_cost(cost):
            robbed = 0

            i = 0

            while i < n:
                if nums[i] <= cost:
                    robbed += 1
                    i += 2
                else:
                    i += 1

            return robbed >= k
            

        n = len(nums)

        left, right = 0, 1_000_000_000

        while left <= right:
            mid = (left + right) // 2

            if is_possible_cost(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left


