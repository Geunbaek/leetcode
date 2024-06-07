
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        dictionary = set(dictionary)

        answer = []
        
        for p in sentence.split():
            temp = ""
            for c in p:
                temp += c
                if temp in dictionary:
                    answer.append(temp)
                    break
            else:
                answer.append(temp)
        return " ".join(answer)
        