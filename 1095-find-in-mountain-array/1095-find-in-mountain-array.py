# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        n = mountain_arr.length() 
        left = 1
        right = n - 2
        answer = n
        top = -1

        while left <= right:
            mid = (left + right) // 2
                
            t = mountain_arr.get(mid)
            l = mountain_arr.get(mid - 1)
            r = mountain_arr.get(mid + 1)
        
            if l < t < r:
                left = mid + 1
            elif l > t > r:
                right = mid - 1
            elif l < t and t > r:
                top = mid
                break
    
        left = 0
        right = top
        
        while left <= right:
            mid = (left + right) // 2
            t = mountain_arr.get(mid)
            
            if target > t:
                left = mid + 1
            elif target < t:
                right = mid - 1
            else:
                answer = min(answer, mid)
                break
            
        left = top
        right = n - 1
        
        while left <= right:
            mid = (left + right) // 2
            t = mountain_arr.get(mid)
            
            if target > t:
                right = mid - 1
            elif target < t:
                left = mid + 1
            else:
                answer = min(answer, mid)
                break
    
        if answer == n:
            return -1
        return answer
                        
                
                    
            
        
        