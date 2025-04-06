class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []

        nums.sort()
        dp = [0 for _ in range(len(nums))]

        for i, num in enumerate(nums):
            _max = 0
            for j in range(0, i):
                if nums[i] % nums[j] == 0:
                    _max = max(_max, dp[j])
            _max += 1
            dp[i] = _max

        _max, index = max([(v, i) for i, v in enumerate(dp)])
        answer = []
        cur_size, cur_tail = _max, nums[index]
        for i in range(index, -1, -1):
            if cur_size == dp[i] and cur_tail % nums[i] == 0:
                answer.append(nums[i])
                cur_size -= 1
                cur_tail = nums[i]
        return answer[::-1]