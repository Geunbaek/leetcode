class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 1_000_000_007

        even = 1
        odd = 0
        prefix_sum = 0
        answer = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2 == 0:
                answer += odd 
                even += 1
            else:
                answer += even 
                odd += 1
            answer %= MOD
        return answer