class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        nums = set()
        n = len(s)
        for i in range(n - k + 1):
            nums.add(s[i: i + k])
        return len(nums) == 2 ** k