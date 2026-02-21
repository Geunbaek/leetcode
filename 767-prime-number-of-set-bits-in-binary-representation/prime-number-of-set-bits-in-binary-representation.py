class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def count_bits(num):
            return bin(num).count('1')
        
        def is_prime(num):
            if num <= 1:
                return False

            for i in range(2, int(math.sqrt(num)) + 1):
                if num % i == 0:
                    return False
            return True
    
        answer = 0
        for num in range(left, right + 1):
            answer += 1 if is_prime(count_bits(num)) else 0
        return answer