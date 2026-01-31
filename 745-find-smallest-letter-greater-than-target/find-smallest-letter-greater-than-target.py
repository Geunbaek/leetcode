class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for letter in sorted(letters):
            if target < letter:
                return letter
        return letters[0]