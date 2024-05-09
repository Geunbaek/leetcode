class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort()
        answer = 0
        for i in range(k):
            _max = happiness.pop()
            if _max >= i:
                answer += _max - i
        return answer