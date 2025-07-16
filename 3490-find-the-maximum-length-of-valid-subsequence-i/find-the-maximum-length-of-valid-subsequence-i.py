class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        even = 0 
        stack = 0
        last = -1
        odd = 0

        for num in nums:
            if num % 2 == 0:
                even += 1

                if stack == 0:
                    last = num
                    stack += 1
                    continue

                if last % 2 != 0:
                    last = num
                    stack += 1
            else:
                odd += 1

                if stack == 0:
                    last = num
                    stack += 1
                    continue

                if last % 2 == 0:
                    last = num
                    stack += 1

        return max(
            even, odd, stack
        )
        