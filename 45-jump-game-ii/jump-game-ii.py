class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        answer = 0

        cur_end, cur_far = 0, 0

        for i in range(n - 1):
            cur_far = max(cur_far, nums[i] + i)

            if i == cur_end:
                answer += 1
                cur_end = cur_far
        return answer
