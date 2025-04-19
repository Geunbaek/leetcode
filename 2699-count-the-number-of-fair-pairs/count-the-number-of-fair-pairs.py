class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        def binary_search(arr, left, right, t):
            while left <= right:
                mid = (left + right) // 2

                if arr[mid] < t:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        nums.sort()
        n = len(nums)
        answer = 0
        for i in range(len(nums)):
            target = nums[i]
            low = binary_search(nums, i + 1, n - 1, lower - target)
            high = binary_search(nums, i + 1, n - 1, upper - target + 1)
    
            answer += high - low
        return answer