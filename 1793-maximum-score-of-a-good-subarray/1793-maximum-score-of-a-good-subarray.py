class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        
        left, right = k, k
        _min = nums[k]
        answer = nums[k]
        
        while left > 0 or right < n - 1:         
            if left > 0 and right < n - 1:
                if nums[left - 1] > nums[right + 1]:
                    _min = min(_min, nums[left - 1])
                    left -= 1
                elif nums[left - 1] < nums[right + 1]:
                    _min = min(_min, nums[right + 1])
                    right += 1
                else:
                    _min = min(_min, nums[right + 1])
                    left -= 1
                    right += 1
            elif left > 0:
                _min = min(_min, nums[left - 1])
                left -= 1
            elif right < n - 1:
                _min = min(_min, nums[right + 1])
                right += 1
            else:
                break
            diff = right - left + 1  
            answer = max(answer, _min * diff)
    
                
        return answer
                    
            
        