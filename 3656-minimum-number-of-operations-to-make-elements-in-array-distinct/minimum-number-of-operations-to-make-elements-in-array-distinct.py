class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter = Counter(nums)
        nums.reverse()
        answer = 0

        while nums:
            if len(counter) == len(nums):
                return answer

            for _ in range(3):
                if nums:
                    num = nums.pop()
                    counter[num] -= 1
                    if counter[num] == 0:
                        del counter[num]
            answer += 1
        return answer