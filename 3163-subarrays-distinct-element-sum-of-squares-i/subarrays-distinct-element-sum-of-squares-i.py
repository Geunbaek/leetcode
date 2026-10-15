class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0
        for i in range(n):
            for j in range(i, n):
                answer += len(set(nums[i : j + 1])) ** 2
        return answer