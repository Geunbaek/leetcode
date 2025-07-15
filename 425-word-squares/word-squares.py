class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
        n, m = len(words), len(words[0])

        cache = [[set() for _ in range(26)] for _ in range(m)]

        for word in words:
            for i, char in enumerate(word):
                j = ord(char) - ord('a')
                cache[i][j].add(word)

        def dfs(depth, path):
            if depth >= m:
                answer.append(path)
                return 

            availables_word = set(words)
            
            for i, word in enumerate(path):
                char = word[depth]
                j = ord(char) - ord('a')
                availables_word &= cache[i][j]
                
            for word in availables_word:
                dfs(depth + 1, path + [word])
        answer = []

        for word in words:
            dfs(1, [word])

        return answer


        