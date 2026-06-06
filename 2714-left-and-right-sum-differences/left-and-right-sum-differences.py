class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = []
        left_sum = [0]
        right_sum = deque([0])
        for i in range(n - 1):
            left_sum.append(left_sum[-1] + nums[i])
            right_sum.appendleft(right_sum[0] + nums[n - i - 1])
        
        for i in range(n):
            answer.append(abs(left_sum[i] - right_sum[i]))
        return answer