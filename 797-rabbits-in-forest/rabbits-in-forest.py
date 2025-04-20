class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        answer = 0
        for i, c in counter.items():
            answer += (i + 1) * math.ceil(c / (i + 1))
        return answer