class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        prev = -101
        cnt = 0

        for num in nums:
            if prev == num:
                cnt += 1
            else:
                nums[i] = num
                prev = num
                i += 1
        return n - cnt