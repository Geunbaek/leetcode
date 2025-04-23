class Solution:
    def countLargestGroup(self, n: int) -> int:
        cache = defaultdict(set)
        _max = 0
        for i in range(1, n + 1):
            _sum = sum(map(int, list(str(i))))
            cache[_sum].add(i)
            _max = max(_max, len(cache[_sum]))

        answer = 0
        for val in cache.values():
            answer += 1 if len(val) == _max else 0
        return answer
