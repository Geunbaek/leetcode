class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n >= 3:
            a = n % 3
            if a > 1:
                return False

            n //= 3

        if n != 1:
            return False
        return True
