class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def get_change_count(num, arr1, arr2):
            count = 0
            for num1, num2 in zip(arr1, arr2):
                if num1 != num and num2 != num:
                    return float("inf")

                if num1 == num:
                    continue
            
                count += 1
            return count

        if tops == bottoms:
            return 0

        _min = float('inf')
        for i in range(1, 7):
            _min = min(_min, get_change_count(i, tops, bottoms))
            _min = min(_min, get_change_count(i, bottoms, tops))

        if _min == float("inf"):
            return -1
        return _min