class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        n = len(nums)

        max_val = 0
        for num in nums:
            max_val |= num

        answer = 0
        def back_tracking(depth, mask):
            nonlocal answer
            if depth >= n:
                if mask == max_val:
                    answer += 1
                return

            
            back_tracking(depth + 1, mask | nums[depth])
            back_tracking(depth + 1, mask)

        back_tracking(0, 0)
        return answer


        