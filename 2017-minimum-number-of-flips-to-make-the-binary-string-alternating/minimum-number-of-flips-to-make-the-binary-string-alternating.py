class Solution:
    def minFlips(self, s: str) -> int:
        odd_dp = [0]
        even_dp = [0]
        n = len(s)
        s = s + s

        for i in range(2 * n):
            if i % 2 == 0 and s[i] == '0':
                odd_dp.append(odd_dp[-1] + 1)
            elif i % 2 != 0 and s[i] == '1':
                odd_dp.append(odd_dp[-1] + 1)
            else:
                odd_dp.append(odd_dp[-1])         

            if i % 2 == 0 and s[i] == '1':
                even_dp.append(even_dp[-1] + 1)
            elif i % 2 != 0 and s[i] == '0':
                even_dp.append(even_dp[-1] + 1)
            else:
                even_dp.append(even_dp[-1])    

        answer = math.inf
        for i in range(n):
            answer = min(answer, odd_dp[i + n] - odd_dp[i], even_dp[i + n] - even_dp[i])
        return answer