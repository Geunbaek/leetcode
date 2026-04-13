class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        answer = len(nums)

        for i, num in enumerate(nums):
            if num == target:
                answer = min(answer, abs(i - start))
        return answer