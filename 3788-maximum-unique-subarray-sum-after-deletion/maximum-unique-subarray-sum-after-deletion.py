class Solution:
    def maxSum(self, nums: List[int]) -> int:
        nums.sort()

        _sum = nums.pop()
        cache = set()
        cache.add(_sum)

        for num in nums[::-1]:
            if num <= 0:
                break

            if num in cache:
                continue
            _sum += num
            cache.add(num)
        return _sum
            