class Solution:
    def countOddLetters(self, n: int) -> int:
        alpha = {
            "0": "zero", "1": "one", "2": "two",
            "3": "three", "4": "four", "5": "five",
            "6": "six", "7": "seven", "8": "eight",
            "9": "nine", "10": "ten"
        }

        answer = 0
        for key, cnt in Counter("".join(map(lambda x: alpha[x], str(n)))).items():      
            if cnt % 2 != 0:
                answer += 1 

        return answer