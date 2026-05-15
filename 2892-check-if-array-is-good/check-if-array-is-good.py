class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        c = Counter(nums)
        c[n - 1] -= 1
        for key, val in c.most_common():
            if key >= n:
                return False
            if val != 1:
                return False
        return True
