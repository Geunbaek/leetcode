class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        for key, value in Counter(nums).items():
            if value % 2 != 0:
                return False

        return True