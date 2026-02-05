class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = []
        for i, num in enumerate(nums):
            if num > 0:
                result.append(nums[(i + num) % n])
            else:
                target = (i - abs(num)) % n
                if target < 0:
                    result.append(nums[n - target])
                else:
                    result.append(nums[target])
        return result 