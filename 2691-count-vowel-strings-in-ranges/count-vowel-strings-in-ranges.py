class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]

        for i, word in enumerate(words):
            start = word[0]
            end = word[-1]

            if start in ["a", "e", "i", 'o', 'u'] and end in ["a", "e", "i", 'o', 'u']:
                prefix_sum.append(prefix_sum[-1] + 1)
            else:
                prefix_sum.append(prefix_sum[-1])

        answer = []
        for i, j in queries:
            answer.append(prefix_sum[j + 1] - prefix_sum[i])

        return answer