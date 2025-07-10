ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]

tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

thousands = ["Billion", "Million", "Thousand", ""]

def toWord(num):
    ret = []
    for i, j in enumerate([100, 10, 1]):
        now = num // j
        if not now:
            continue
        
        if i == 0 and now:
            ret.append(f"{ones[now]} Hundred")
        else:
            if i == 1: 
                if 1 <= num < len(ones):
                    ret.append(ones[num])
                    break
                else:
                    ret.append(tens[now])
            else:
                ret.append(ones[now])
        num %= j
    return " ".join(ret)


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        answer = []
        for i, j in enumerate([1_000_000_000, 1_000_000, 1_000, 1]):
            word = toWord(num // j)
            if word:
                answer.append(f"{word} {thousands[i]}")
            num %= j

        return " ".join(answer).strip()

        