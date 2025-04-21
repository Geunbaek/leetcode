class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        prefix_sum = [0]
        _min = 0
        _max = 0

        for diff in differences:
            cur = prefix_sum[-1] + diff
            prefix_sum.append(cur)
            _min = min(_min, cur)
            _max = max(_max, cur)

            if (_max - _min) > upper - lower:
                return 0

        return (upper - lower) - (_max - _min) + 1
