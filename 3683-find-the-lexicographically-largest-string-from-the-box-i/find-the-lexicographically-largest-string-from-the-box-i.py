class Solution:
    def answerString(self, word: str, numFriends: int) -> str:

        if numFriends == 1:
            return word

        max_length = len(word) - numFriends + 1

        answer = []

        target = sorted(word, reverse=True)[0]

        for i in range(len(word)):
            if word[i] == target:
                answer.append(word[i: i + max_length])

        return sorted(answer, reverse=True)[0]

        