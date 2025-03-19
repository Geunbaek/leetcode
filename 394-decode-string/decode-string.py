class Solution:
    def decodeString(self, s: str) -> str:
        def recur(depth):
            digit = ""
            ret = ""
            i = depth

            while i < n:
                if s[i] == "[":
                    end, word = recur(i + 1)
                    ret += int(digit) * word
                    i = end + 1
                    digit = ""
                    continue

                if s[i] == "]":
                    return (i, ret)
                
                if s[i].isdigit():
                    digit += s[i]
                else:
                    ret += s[i]
                i += 1

            return ret

        n = len(s)
        return recur(0)