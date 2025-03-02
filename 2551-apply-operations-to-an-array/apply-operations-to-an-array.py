class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        
        zero = nums.count(0)
        answer = list(filter(lambda x: x != 0, nums))

        for i in range(zero):
            answer.append(0)
        return answer