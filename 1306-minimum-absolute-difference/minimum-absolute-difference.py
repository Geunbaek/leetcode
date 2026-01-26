class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        h = []
        arr.sort()
        for n1, n2 in zip(arr, arr[1:]):
            heapq.heappush(h, (abs(n2 - n1), n1, n2))

        min_diff = h[0][0]
        answer = []
        while h:
            diff, n1, n2 = heapq.heappop(h)
            if min_diff == diff:
                answer.append([n1, n2])
            else:
                break
        return answer