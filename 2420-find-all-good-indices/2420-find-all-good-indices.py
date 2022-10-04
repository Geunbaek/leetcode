class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        increaseArr = [1]
        decreaseArr = [-1]
        answer = []

        for i in range(1, len(nums)):
            if nums[i - 1] <= nums[i]:
                increaseArr.append(increaseArr[-1] + 1)
            else:
                increaseArr.append(1)
        
        for i in range(1, len(nums)):
            if nums[i - 1] >= nums[i]:
                decreaseArr.append(decreaseArr[-1] - 1)
            else:
                decreaseArr.append(-1)
        for i in range(len(nums)):
            if i - k >= 0 and i + k < len(nums):
                if increaseArr[i + k] >= k and decreaseArr[i - 1] <= -k:
                    answer.append(i)

        return answer 
                