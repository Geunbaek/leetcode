class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2

        self.cache = defaultdict(int)
        for num in nums2:
            self.cache[num] += 1

    def add(self, index: int, val: int) -> None:
        prev = self.nums2[index]
        _next = prev + val
        self.cache[prev] -= 1
        self.nums2[index] = _next
        self.cache[_next] += 1

    def count(self, tot: int) -> int:
        count = 0
        for num in self.nums1:
            diff = tot - num
            count += self.cache[diff]
        return count



# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)