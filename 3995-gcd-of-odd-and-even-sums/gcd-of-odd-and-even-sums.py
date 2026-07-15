class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        sum_odd = 0
        sum_even = 0
        cnt = 0
        for i in range(1, 10001, 2):
            sum_odd += i
            sum_even += i + 1   
            cnt += 1
            if cnt == n:
                break
        return gcd(sum_odd, sum_even)