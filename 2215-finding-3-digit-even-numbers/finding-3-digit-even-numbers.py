

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        answer = set()
        for perm in permutations(digits, 3):
            num = int("".join(perm))
            if not (100 <= num <= 999):
                continue
            if num % 2 != 0:
                continue
            answer.add(num)
        return sorted(answer)