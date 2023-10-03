class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        answer = 0
        for key, val in Counter(nums).items():
            if val <= 1: continue
            answer += ((val - 1) * val) // 2
        return answer