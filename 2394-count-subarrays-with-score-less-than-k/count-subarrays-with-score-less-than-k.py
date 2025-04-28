class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        prefix = 0
        left = 0
        answer = 0

        for right in range(len(nums)):
            prefix += nums[right]

            while left <= right and prefix * (right - left + 1) >= k:
                prefix -= nums[left]
                left += 1
            answer += right - left + 1
        return answer
                
