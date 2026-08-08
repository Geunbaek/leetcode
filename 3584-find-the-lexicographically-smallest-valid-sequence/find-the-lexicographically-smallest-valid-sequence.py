class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n = len(word1)
        m = len(word2)

        last = [-1 for _ in range(m)]
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        answer = []
        skip = 0
        j = 0
        for i, c in enumerate(word1):
            if j == m:
                break
            if c == word2[j] or (skip == 0 and (j == m - 1 or i < last[j + 1])):
                answer.append(i)
                skip += (c != word2[j])
                j += 1
        return answer if j == m else []


            