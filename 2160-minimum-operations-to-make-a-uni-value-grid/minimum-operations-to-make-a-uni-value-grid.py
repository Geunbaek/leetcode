class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []

        for line in grid:
            arr.extend(line)

        arr.sort()
        mid = arr[len(arr) // 2]
        count = 0
        for num in arr:
            if abs(mid - num) % x != 0:
                return -1

            count += abs(mid - num) // x
        return count


        