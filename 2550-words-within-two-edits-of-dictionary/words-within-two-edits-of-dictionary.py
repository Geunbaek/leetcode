class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        def is_one_diff(word1, word2):
            count = 0
            for w1, w2 in zip(word1, word2):
                if w1 != w2:
                    count += 1
            return count <= 2

        answer = []
        for query in queries:
            for word in dictionary:
                if is_one_diff(query, word):
                    answer.append(query)
                    break
        return answer