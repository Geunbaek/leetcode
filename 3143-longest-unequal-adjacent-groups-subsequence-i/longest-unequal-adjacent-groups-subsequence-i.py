class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)

        answer = [words[0]]

        for i in range(1, n):
            if groups[i] != groups[i - 1]:
                answer.append(words[i])

        return answer