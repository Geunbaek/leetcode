class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        answers = []
        
        for letter in letters:
            if ord(letter) > ord(target):
                answers.append(letter)
        if answers:
            return answers[0]
        return letters[0]
        