class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        answer = 0

        for i in range(n):
            for j in range(i + 1, n):
                word1 = words[i]
                word2 = words[j]
                if word2.startswith(word1) and word2.endswith(word1):
                    answer += 1
        return answer