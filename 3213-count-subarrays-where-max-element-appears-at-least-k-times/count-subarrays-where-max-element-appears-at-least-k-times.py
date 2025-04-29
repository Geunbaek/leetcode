class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        _max = max(nums)
        n = len(nums)
        answer = 0

        right = 0
        max_count = 0

        for left in range(n):
            while right < n and max_count < k:
                if _max == nums[right]:
                    max_count += 1
                right += 1

            if max_count >= k:
                answer += n - right + 1

            if nums[left] == _max:
                max_count -= 1

        return answer
            