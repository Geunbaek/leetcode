class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        answer = []

        for i in range(n):
            temp_a = A[: i + 1]
            temp_b = set(B[: i + 1])

            temp = 0
            for num in temp_a:
                if num in temp_b:
                    temp += 1
            answer.append(temp)
        return answer


        