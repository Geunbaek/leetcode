class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        answer = 0

        count = defaultdict(int)

        for i in range(len(nums)):
            for j in range(i):
                product = nums[i] * nums[j]

                answer += count[product] * 8
                count[product] += 1

        return answer