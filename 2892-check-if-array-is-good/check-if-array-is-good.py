class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        c = Counter(nums)
        c[n - 1] -= 1
        for i in range(1, n):
            if i not in c:
                return False
            c[i] -= 1

        for key, val in c.most_common():
            if val != 0:
                return False
        return True
