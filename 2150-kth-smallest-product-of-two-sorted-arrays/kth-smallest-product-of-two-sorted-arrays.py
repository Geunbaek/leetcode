class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def calc_less_count(target):
            less_count = 0

            for num in nums1:
                if num == 0:
                    if target >= 0:
                        less_count += len(nums2)
                    continue
                
                if num < 0:
                    less_count += len(nums2) - bisect_left(nums2, ceil(target / num))
                else:
                    less_count += bisect_right(nums2, target // num)
            return less_count

        MIN = -(100_000 * 100_000)
        MAX = (100_000 * 100_000)
        l, r = MIN, MAX

        while l <= r:
            mid = (l + r) // 2
            if calc_less_count(mid) >= k:
                r = mid - 1
            else:
                l = mid + 1
        return l