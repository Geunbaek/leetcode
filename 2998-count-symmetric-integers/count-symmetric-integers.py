class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        answer = 0

        for i in range(low, high + 1):
            str_num = str(i)
            if len(str_num) % 2 != 0:
                continue

            mid = (len(str_num) // 2)
            left = list(map(int, str_num[:mid]))
            right = list(map(int, str_num[mid:]))

            if sum(left) == sum(right):
                answer += 1

        return answer


