class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def recur(depth, word):
            if depth >= n:
                words.append(word)
                return

            for char in ["a", "b", "c"]:
                if word and word[-1] == char:
                    continue
                recur(depth + 1, word + char)

        words = []
        recur(0, "")
        if len(words) < k:
            return ""
        return words[k - 1]