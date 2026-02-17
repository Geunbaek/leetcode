class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        def get_time():
            h = int("".join(map(str, time[:4])), 2)
            m = int("".join(map(str, time[4:])), 2)

            if not 0 <= h < 12:
                return (-1, -1)
            if not 0 <= m < 60:
                return (-1, -1)
            return (h, m)

        def recur(depth, count):
            if count >= turnedOn:
                h, m = get_time()
                if h != -1:
                    answer.append(f"{h}:{str(m).zfill(2)}")
                return
            
            if depth >= 10:
                return

            time[depth] = 1
            recur(depth + 1, count + 1)
            time[depth] = 0
            recur(depth + 1, count)
        answer = []
        time = [0 for _ in range(10)]
        recur(0, 0)

        return answer


