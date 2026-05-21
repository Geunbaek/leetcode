class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        num1_set = set()
        for num in arr1:
            while num >= 10:
                num1_set.add(num)
                num //= 10
            num1_set.add(num)

        answer = 0
        for num in arr2:
            while num >= 10:
                if num in num1_set:
                    answer = max(answer, len(str(num)))
                num //= 10
            if num in num1_set:
                answer = max(answer, len(str(num)))
        return answer