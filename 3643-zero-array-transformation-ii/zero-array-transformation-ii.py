class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def can_zero_array(k):
            n = len(nums)
            prefix = [0 for _ in range(n + 1)]

            for l, r, v in queries[:k]:
                prefix[l] += v
                prefix[r + 1] -= v
            
            total = 0

            for i, num in enumerate(prefix[:-1]):
                total += num
                if total < nums[i]:
                    return False
            return True
        
        left = 0
        right = len(queries)

        if not can_zero_array(right):
            return -1

        while left <= right:
            mid = (left + right) // 2

            if can_zero_array(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left

