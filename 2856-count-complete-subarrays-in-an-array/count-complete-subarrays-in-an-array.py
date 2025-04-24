class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        counter = Counter(nums)
        m = len(counter)
        n = len(nums)

        cache = {}
        right = 0
        answer = 0

        for left in range(n):
            counter = set()
            for right in range(left, n):
                counter.add(nums[right])

                if len(counter) == m:
                    answer += 1

        return answer

            