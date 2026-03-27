class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        r, c = len(mat), len(mat[0])
        temp = [row[::] for row in mat]
        k %= c
        def shift_left(y):
            first = temp[y][0]
            for x in range(c - 1):
                temp[y][x] = temp[y][x + 1]
            temp[y][-1] = first

        def shift_right(y):
            last = temp[y][-1]
            for x in range(c - 1, 0, -1):
                temp[y][x] = temp[y][x - 1]
            temp[y][0] = last

        def _shift():
            for y in range(r):
                if y % 2 == 0:
                    shift_left(y)
                else:
                    shift_right(y)

        def is_equal():
            for y in range(r):
                for x in range(c):
                    if temp[y][x] != mat[y][x]:
                        return False
            return True

        for _ in range(k):
            _shift()
        return is_equal()