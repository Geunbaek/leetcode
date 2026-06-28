class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        answer = 0
        last = 0
        for num in arr:
            if num == last:
                continue
            if num > last:
                answer += 1
                last += 1
        return answer