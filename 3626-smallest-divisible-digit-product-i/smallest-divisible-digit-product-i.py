class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def mul(arr):
            ret = 1

            for num in arr:
                ret *= num

            return ret

        for i in range(n, 1000):
            _sum = mul(list(map(int, str(i))))
            if _sum % t == 0:
                return i
        return -1