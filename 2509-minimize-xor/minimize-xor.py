class Solution:    
    def minimizeXor(self, num1: int, num2: int) -> int:
        bin_num2 = bin(num2)
        one = bin_num2.count("1")

        answer = 0

        set_bits_count = 0
        current_bit = 31 

        while set_bits_count < one:
            if (num1 & (1 << current_bit)) != 0 or (
                one - set_bits_count > current_bit
            ):
                answer = answer | (1 << current_bit)
                set_bits_count += 1
            current_bit -= 1 

        return answer

        def recur(depth, z, value):
            if z == zero:
                print(value)
                return

            if depth >= 9:
                return

            for i in range(9):
                v

        return num1 ^ num2