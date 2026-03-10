class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7
        
        # 1. 팩토리얼 및 역원 사전 계산 (조합 nCr을 O(1)에 구하기 위함)
        MAX = zero + one + 1
        fact = [1] * MAX
        inv = [1] * MAX
        
        for i in range(1, MAX):
            fact[i] = (fact[i - 1] * i) % MOD
            
        # 페르마의 소정리를 이용한 모듈로 역원 계산
        inv[MAX - 1] = pow(fact[MAX - 1], MOD - 2, MOD)
        for i in range(MAX - 2, -1, -1):
            inv[i] = (inv[i + 1] * (i + 1)) % MOD
            
        def nCr(n, r):
            if r < 0 or r > n:
                return 0
            return fact[n] * inv[r] % MOD * inv[n - r] % MOD

        # 2. 포함-배제의 원리가 적용된 핵심 수학 함수
        def ways(n, k, l):
            """
            n개의 동일한 아이템을 k개의 그룹으로 나누되, 
            각 그룹의 크기가 l 이하가 되도록 하는 경우의 수
            """
            if k == 0:
                return 1 if n == 0 else 0
            if n < k or n > k * l:
                return 0
            
            res = 0
            max_i = (n - k) // l
            
            # i는 한도(l)를 초과하여 '규칙을 위반한' 그룹의 개수
            for i in range(max_i + 1):
                # 위반할 그룹을 고르는 경우의 수
                ways_to_choose_violators = nCr(k, i)
                # 남은 아이템들을 분배하는 경우의 수 (중복 조합)
                ways_to_distribute_rest = nCr(n - i * l - 1, k - 1)
                
                term = (ways_to_choose_violators * ways_to_distribute_rest) % MOD
                
                # 포함-배제의 원리: 홀수 개 위반은 빼고, 짝수 개 위반은 더함
                if i % 2 == 1:
                    res = (res - term + MOD) % MOD
                else:
                    res = (res + term) % MOD
            return res

        total_ways = 0
        
        # 3. 0의 묶음(블록) 개수 k를 기준으로 가능한 모든 교대 배열 조합 계산
        for k in range(1, zero + 1):
            ways0 = ways(zero, k, limit)
            if ways0 == 0:
                continue
            
            # 1의 묶음이 될 수 있는 개수는 k-1, k, k+1 세 가지뿐입니다.
            
            # 케이스 A: 0 묶음으로 시작해서 0 묶음으로 끝나는 경우 (1의 묶음은 k-1개)
            ways1_1 = ways(one, k - 1, limit)
            
            # 케이스 B & C: 0으로 시작해 1로 끝나거나, 1로 시작해 0으로 끝나는 경우 (1의 묶음은 k개)
            ways1_2 = ways(one, k, limit)
            
            # 케이스 D: 1 묶음으로 시작해서 1 묶음으로 끝나는 경우 (1의 묶음은 k+1개)
            ways1_3 = ways(one, k + 1, limit)
            
            # 모든 경우의 수를 누적
            total_ways = (total_ways + ways0 * ways1_1) % MOD
            total_ways = (total_ways + ways0 * ways1_2 * 2) % MOD # 대칭 구조이므로 * 2
            total_ways = (total_ways + ways0 * ways1_3) % MOD
            
        return total_ways