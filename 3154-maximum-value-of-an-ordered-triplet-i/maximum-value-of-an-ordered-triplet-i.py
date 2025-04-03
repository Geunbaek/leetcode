class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        answer = 0
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    value = (nums[i] - nums[j]) * nums[k]
                    answer = max(answer, value)

        return answer