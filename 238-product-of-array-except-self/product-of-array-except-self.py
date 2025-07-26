class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l = [1]

        for num in nums:
            l.append(l[-1] * num)

        r = deque([1])
        for num in nums[::-1]:
            r.appendleft(r[0] * num)

        answer = []

        for i in range(1, n + 1):
            answer.append(l[i - 1] * r[i])

        return answer
