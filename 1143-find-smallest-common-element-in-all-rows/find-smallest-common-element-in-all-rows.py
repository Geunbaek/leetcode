class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])

        pointers = [0 for _ in range(n)]

        def get_max_by_row(mat):
            _max = -float("inf")
            for y in range(n):
                _max = max(_max, mat[y][pointers[y]])

            return _max

        while True:
            _max = get_max_by_row(mat)
            is_change = False

            for y, pointer in enumerate(pointers):
                if _max > mat[y][pointer]:
                    is_change = True
                    pointers[y] += 1
                    if pointers[y] >= m:
                        return -1

            if not is_change:
                return _max

        return -1



        