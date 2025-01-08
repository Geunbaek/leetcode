class Solution:
    def equalDigitFrequency(self, s: str) -> int:

        n = len(s)
        answer = set()

        for left in range(n):
            counter = [0 for _ in range(10)]

            for right in range(left, n):
                counter[int(s[right])] += 1
                cur_count = 0
                is_valid = True

                for count in counter:
                    if count == 0:
                        continue

                    if cur_count == 0:
                        cur_count = count
                    
                    if cur_count != count:
                        is_valid = False
                        break
                if is_valid:
                    answer.add(s[left: right + 1])
        print(answer)
        return len(answer)

