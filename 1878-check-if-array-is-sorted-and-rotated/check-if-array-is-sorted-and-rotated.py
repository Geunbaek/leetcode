class Solution:
    def check(self, nums: List[int]) -> bool:
        temp = deque(nums)

        _max = max(nums)
        _min = min(nums)

        while temp[-1] < _max:
            temp.rotate(1)

        while temp[0] > _min:
            temp.rotate(-1)

        return sorted(nums) == list(temp)