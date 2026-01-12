class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        count = Counter(s).most_common()
        h = []
        h2 = []

        for key, cnt in count:
            heappush(h, (-ord(key), key, cnt))

        answer = []
        while h:
            i, key, cnt = heappop(h)
            used = 0

            while h2 and h2[0][0] > i:
                heappush(h, heappop(h2))

            if h2:
                used = 1
            else:
                used = min(cnt, repeatLimit)
            answer.append((key, used))
                
            print(key, h2)
            while h2:
                heappush(h, heappop(h2))
            
            if cnt > used:
                heappush(h2, (-ord(key), key, cnt - used))

        return "".join(map(lambda x: x[0] * x[1], answer))