class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        left = 0
        right = sum(nums)
        answer = 0
        
        for i, num in enumerate(nums[:-1]):
            left += num
            right -= num

            if left >= right:
                answer += 1
        return answer
