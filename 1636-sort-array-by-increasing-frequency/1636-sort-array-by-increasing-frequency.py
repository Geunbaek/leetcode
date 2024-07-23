class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        print(counter[2])
        nums.sort(key = lambda x: (counter[x], -x))
        return nums