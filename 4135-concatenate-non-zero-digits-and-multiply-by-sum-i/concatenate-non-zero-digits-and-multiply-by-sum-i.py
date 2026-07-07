class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n == 0:
            return 0
        nums = list(filter(lambda x: x != 0, map(int, list(str(n)))))
        return int("".join(map(str, nums))) * sum(nums)