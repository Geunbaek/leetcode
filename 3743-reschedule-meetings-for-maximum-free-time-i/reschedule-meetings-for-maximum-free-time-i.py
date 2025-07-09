class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        intervals = []

        if startTime[0] != 0:
            intervals.append(startTime[0])

        for end, start in zip(endTime, startTime[1:]):
            intervals.append(start - end)

        if endTime[-1] != eventTime:
            intervals.append(eventTime - endTime[-1])

        prefix_sum = [0]

        for interval in intervals:
            prefix_sum.append(prefix_sum[-1] + interval)
        answer = 0
        for i in range(k + 1, len(prefix_sum)):
            answer = max(answer, prefix_sum[i] - prefix_sum[i - (k + 1)])

        if len(prefix_sum) <= k + 1:
            answer = prefix_sum[-1] - prefix_sum[0]

        return answer

            