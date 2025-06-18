class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        answer = []

        for i in range(0, len(nums), 3):
            now = nums[i: i + 3]
            if now[-1] - now[0] > k:
                return []
            answer.append(now)
        return answer