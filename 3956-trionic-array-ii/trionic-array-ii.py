class Solution:
    def maxSumTrionic(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        ans = -float('inf')

        while i < n - 1:
            if nums[i] <= nums[i + 1]:
                i += 1
                continue

            p = i
            q = i
            mid_sum = nums[q]
            while q < n - 1 and nums[q] > nums[q + 1]:
                q += 1 
                mid_sum += nums[q]

            if p - 1 < 0 or nums[p] == nums[p - 1]:
                i = q
                continue

            l = p - 1
            left_sum = nums[l]
            left_max = left_sum
            while l - 1 >= 0 and nums[l] > nums[l - 1]:
                l -= 1
                left_sum += nums[l]
                left_max = max(left_max, left_sum)

            if l == p:
                i = q
                continue

            if q + 1 >= n or nums[q] == nums[q + 1]:
                i = q
                continue

            r = q + 1
            right_sum = nums[r]
            right_max = right_sum
            while r + 1 < n and nums[r] < nums[r + 1]:
                r += 1
                right_sum += nums[r]
                right_max = max(right_max, right_sum)

            if r == q:
                i = q
                continue
            
            _sum = left_max + mid_sum + right_max
            print(left_max, mid_sum, right_max)
            print(l, p, q, r)
            print(_sum)
            ans = max(ans, _sum)
            i = q

        return ans
