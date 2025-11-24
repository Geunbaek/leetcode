class Solution(object):
    def prefixesDivBy5(self, nums):
        now = 0
        answer = []
        for i, num in enumerate(nums):
            now += num
            answer.append(now % 5 == 0)
            now *= 2
        return answer
            