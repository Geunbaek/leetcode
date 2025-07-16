class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        evens = []    
        stack = []
        odds = []

        for num in nums:
            if num % 2 == 0:
                evens.append(num)

                if not stack:
                    stack.append(num)
                    continue
                if stack[-1] % 2 != 0:
                    stack.append(num)
            
            else:
                odds.append(num)

                if not stack:
                    stack.append(num)
                    continue
                if stack[-1] % 2 == 0:
                    stack.append(num)

        return max(
            len(evens), len(odds), len(stack)
        )
        