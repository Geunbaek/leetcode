class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left, right = 0, len(height)-1
        lm, rm = height[left], height[right]
        volume = 0
        
        while left < right:
            lm, rm = max(lm, height[left]), max(rm, height[right])
            
            if height[left] <= height[right]:
                volume += lm - height[left]
                left += 1
            else:
                volume += rm - height[right]
                right -=1
        return volume
