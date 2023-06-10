class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        left = index
        right = n - index - 1
        
        def _sum(value):
            left_value = value - 1
            right_value = value - 1
            
            if left <= 0:
                left_sum =0
            elif left > left_value:
                ones = left - left_value
                left_sum = left_value * (left_value + 1) // 2 + ones
            else:
                last_num = left_value - left + 1
                m = left_value + last_num
                left_sum = m * left // 2
              
            if right <= 0:
                right_sum =0
            elif right > right_value:
                ones = right - right_value
                right_sum = right_value * (right_value + 1) // 2 + ones
            else:
                last_num = right_value - right + 1
                m = right_value + last_num
                right_sum = m * right // 2
            print(left_sum, right_sum)
            return left_sum + right_sum + value
        
        
        l, r = 1, maxSum
        
        while l <= r:
            mid = (l + r) // 2
            print(mid, "mid")
            print(_sum(mid))
            if _sum(mid) <= maxSum:
                l = mid + 1
            else:
                r = mid - 1
        return r

 