class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = list(filter(lambda x: x % 2 == 0, nums))
        odds = list(filter(lambda x: x % 2 != 0, nums))

        stack = []

        for num in nums:
            if not stack:
                stack.append(num)
                continue
            
            if stack[-1] % 2 == 0 and num % 2 != 0:
                stack.append(num)

            if stack[-1] % 2 != 0 and num % 2 == 0:
                stack.append(num)

        print(evens)
        print(odds)
        print(stack)
        return max(
            len(evens), len(odds), len(stack)
        )
        