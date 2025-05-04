class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        def get_comb(n, r):
            upper = 1

            for i in range(r):
                upper *= n - i
            return upper // factorial(r)

        cache = {}

        for domino in dominoes:
            sorted_domino = tuple(sorted(domino))
            cache[sorted_domino] = cache.get(sorted_domino, 0) + 1

        answer = 0
        for val in cache.values():
            if val >= 2:
                answer += get_comb(val, 2)
        return answer