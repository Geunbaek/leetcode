class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        for num, cnt in Counter(nums).items():
            temp = cnt
            
            if temp % 3 == 0:
                ans += temp // 3
            else:
                while temp > 0:
                    temp -= 2
                    ans += 1
                    if temp % 3 == 0:
                        ans += temp // 3
                        temp %= 3
                if temp != 0:
                    return -1
                
        return ans
