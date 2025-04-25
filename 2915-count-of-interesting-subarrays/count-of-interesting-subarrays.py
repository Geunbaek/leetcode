class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        prefix_sum = 0
        cnt = {0: 1}
        
        answer = 0

        for num in nums:
            if num % modulo == k:
                prefix_sum += 1

            now = prefix_sum % modulo
            prev = (prefix_sum - k) % modulo
            answer += cnt.get(prev, 0)
            cnt[now] = cnt.get(now, 0) + 1
        return answer
        