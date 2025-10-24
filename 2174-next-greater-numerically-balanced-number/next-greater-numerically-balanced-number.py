class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def isBalancedNumber(num):
            for key, value in Counter(str(num)).items():
                if int(key) != value:
                    return False
                
            return True
        for i in range(n + 1, 10_000_000):  
            if isBalancedNumber(i):
                return i

        return -1
        