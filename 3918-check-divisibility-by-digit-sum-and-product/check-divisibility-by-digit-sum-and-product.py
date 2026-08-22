class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def mul(nums):
            i = 1

            for num in nums:
                i *= num
            return i

        nums = list(map(int, list(str(n))))

        _sum = sum(nums) + mul(nums)
        return n % _sum == 0