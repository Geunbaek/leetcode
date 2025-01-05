class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)

        letters = [ord(c) - ord("a") for c in s]

        dp = [0 for _ in range(n + 1)]

        for s, e, d in shifts:
            if d == 0:
                dp[s] -= 1
                dp[e + 1] += 1
            else:
                dp[s] += 1
                dp[e + 1] -= 1

        prefix_sum = [0]

        for i in range(n):
            prefix_sum.append(prefix_sum[-1] + dp[i])

        answer = []

        for i in range(1, n + 1):
            letter = letters[i - 1] + prefix_sum[i]

            if letter < 0:
                diff = -letter // 26
                letter += 26 * (diff + 1)


            if letter >= 26:
                letter %= 26

            answer.append(chr(letter + ord('a')))

        return "".join(answer)



        