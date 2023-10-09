class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        answer = [n, -1]
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                answer[0] = min(answer[0], mid)
                right = mid - 1
        
        left = 0
        right = n - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                answer[1] = max(answer[1], mid)
                left = mid + 1
        
        if answer[0] == n:
            return [-1, -1]
        return answer
        
                
                

        
        