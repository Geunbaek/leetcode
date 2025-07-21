class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        copy_nums = nums[:]

        for i in range(k, k + n):
            nums[i % n] = copy_nums[i - k]
        

