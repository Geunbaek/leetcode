class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        cache = defaultdict(list)

        for i, num in enumerate(nums):
            cache[num].append(i)

        def calc_tuple_dist(i, j, k):
            print(i, j, k)
            return abs(i - j) + abs(j - k) + abs(k - i)

        answer = -1
        for key, ns in cache.items():
            if len(ns) < 3:
                continue
            for i in range(len(ns) - 2):
                tuple_dist = calc_tuple_dist(ns[i], ns[i + 1], ns[i + 2])
                print(tuple_dist)
                if answer == -1:
                    answer = tuple_dist
                else:
                    answer = min(answer, tuple_dist)

        return answer