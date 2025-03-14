class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(num):
            d = 0

            for candy in candies:
                d += candy // num
            return d >= k

        if sum(candies) < k:
            return 0

        left, right = 1, 10_000_000

        while left <= right:
            mid = (left + right) // 2

            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right