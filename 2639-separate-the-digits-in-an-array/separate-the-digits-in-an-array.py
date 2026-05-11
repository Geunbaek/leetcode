class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ret = []

        for num in nums:
            ret.extend(list(map(lambda x: int(x), str(num))))
        return ret