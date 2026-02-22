class Solution:
    def binaryGap(self, n: int) -> int:
        answer = 0

        bits = bin(n)[2:]
        m = len(bits)
        l, r = 0, 0

        while l < m:
            if bits[l] == '0':
                l += 1
                continue
            r = l + 1
            while r < m and bits[r] == '0':
                r += 1
            if r < m:
                answer = max(answer, r - l)
            l = r
        return answer

