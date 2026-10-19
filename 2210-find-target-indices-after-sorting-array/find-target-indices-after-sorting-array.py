class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return list(map(lambda x: x[0], filter(lambda x: x[1] == target, enumerate(sorted(nums)))))