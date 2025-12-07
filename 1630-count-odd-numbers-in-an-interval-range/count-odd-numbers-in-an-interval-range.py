class Solution:
    def countOdds(self, low: int, high: int) -> int:
        count = high - low + 1
        if high % 2 == 0: count -= 1
        if low % 2 == 0: count -= 1
        return (count // 2) + 1