class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache
        def recur(n, sub_sum):
            if sub_sum == 0:
                return True

            if n == 0 or sub_sum < 0:
                return False

            result = recur(n - 1, sub_sum - nums[n - 1]) or recur(n - 1, sub_sum)

            return result

        n = len(nums)

        total = sum(nums)
        if total % 2 != 0:
            return False

        subset_sum = total // 2
        n = len(nums)
        return recur(n - 1, subset_sum)