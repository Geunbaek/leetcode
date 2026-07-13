class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        nums = [i for i in range(1, 10)]
        answer = []
        for k in range(1, 10):
            for i in range(10):
                if i + k >= 10:
                    continue
                num = int("".join(map(str, nums[i: i + k])))
                if low <= num <= high:
                    answer.append(num)
        return answer